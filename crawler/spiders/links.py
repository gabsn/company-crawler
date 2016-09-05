# coding: utf-8

import re

from mongoengine import Document
from mongoengine.fields import StringField, ListField

from scrapy.http import Request
from scrapy.spiders import Spider

from crawler.items import LinksItem
from utils.mongodb import connect_mongoengine

RE_COMPANY_PAGE = re.compile(r'https?://www\.linkedin\.com/company/.+')
RE_PARENT = re.compile(r'((-?[^-]+)+)-[^-]+')
RE_DIRECTORY = re.compile(
    r'https?://www\.linkedin\.com/directory/companies-(.+)/'
)


def get_dir(url):
    m_dir = RE_DIRECTORY.search(url)
    if m_dir:
        return m_dir.group(1)


def get_parent(directory):
    m_parent = RE_PARENT.search(directory)
    if m_parent:
        return m_parent.group(1)


def get_node(directory):
    try:
        node = Node.objects(name=directory).get()
    except:
        node = Node(name=directory).save()

    return node


def is_leaf(hrefs):
    return RE_COMPANY_PAGE.match(hrefs[0])


def update_childs(node, childs):
    Node.objects(name=node.name).update(set__childs=childs, upsert=True)


def update_parent_with_leaf(node):
    Node.objects(name=get_parent(node.name)) \
        .update(push__leaves=node.name, upsert=True)


class Node(Document):
    meta = {'collection': 'crawling_tree'}
    name = StringField(primary_key=True)
    childs = ListField(default=[])
    leaves = ListField(default=[])


class LinksSpider(Spider):
    """Spider getting all company urls

    We need to crawl linkedin tree in DFO order

    """

    name = "Links"
    collection = "linkedin_links"
    start_urls = ['https://www.linkedin.com']

    def __init__(self):
        super(LinksSpider, self).__init__()
        connect_mongoengine()

    def parse(self, response):
        """First request needed to get cookies"""
        yield Request(
            url="https://www.linkedin.com/directory/companies/",
            callback=self.parse_by_name)

    def parse_by_name(self, response):
        """Browse by name"""
        for href in response.xpath('//*[@class="bucket-list"]//@href'):
            yield Request(
                url=href.extract(),
                callback=self.parse_all_links)

    def parse_all_links(self, response):
        hrefs = response.xpath('//*[@class="columns"]//@href').extract()
        childs = [get_dir(href) for href in hrefs]

        node = get_node(get_dir(response.url))
        update_childs(node, childs)

        # Current directory is a leaf
        if is_leaf(hrefs):
            item = LinksItem()

            for href in hrefs:
                item['url'] = href
                yield item

            update_parent_with_leaf(node)

        # Current directory is an internal node
        else:
            for href in hrefs:
                child = get_dir(href)

                if child not in node.leaves:
                    yield Request(
                        url=href,
                        callback=self.parse_all_links)
