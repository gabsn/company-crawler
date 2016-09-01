# coding: utf-8

import re, logging, pdb

from mongoengine import Document, connect
from mongoengine.fields import *

from scrapy.http import Request
from scrapy.spiders import BaseSpider

from linkedin_crawler.items import LinkedinCrawlerItem
from linkedin_crawler.settings import MONGODB_CONFIG

RE_COMPANY_PAGE = re.compile(r'https?://www\.linkedin\.com/company/.+')
RE_PARENT = re.compile(r'((-?[^-]+)+)-[^-]+')
RE_DIRECTORY = re.compile(
    r'https?://www\.linkedin\.com/directory/companies-(.+)/'
)

HEADERS = {
    'user-agent': (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 "
        "Safari/537.36"
    ),
    'accept': (
        "text/html,application/xhtml+xml,application/xml;"
        "q=0.9,image/webp,*/*;q=0.8"),
    'referer': "https://www.linkedin.com",
    'accept-encoding': "gzip, deflate, br",
    'accept-language': "en-US,en;q=0.8",
}


def connect_mongoengine():
    connect(
            db=MONGODB_CONFIG['db'],
            username=MONGODB_CONFIG['username'],
            password=MONGODB_CONFIG['password'],
            host=MONGODB_CONFIG['host'],
            port=MONGODB_CONFIG['port'],
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
    if RE_COMPANY_PAGE.match(hrefs[0]):  
        return True
    else:
        return False


def update_childs(node, childs):
    Node.objects(name=node.name).update(set__childs=childs, upsert=True)


def update_parent_with_leaf(node):
    Node.objects(name=get_parent(node.name)).update(push__leaves=node.name, upsert=True)


class Node(Document):
    meta = {'collection': 'crawling_tree'}
    name = StringField(primary_key=True)
    childs = ListField(default=[])
    leaves = ListField(default=[])


class LinkedinLinksSpider(BaseSpider):
    """Spider getting all company urls

    We need to crawl linkedin tree in DFO order

    """

    name = "LinkedinLinksSpider"
    start_urls = ['https://www.linkedin.com']

    def __init__(self):
        super(LinkedinLinksSpider, self).__init__()
        connect_mongoengine()
        
    def parse(self, response):
        """First request needed to get cookies"""
        yield Request(
            url="https://www.linkedin.com/directory/companies/",
            callback=self.parse_by_name)

    def parse_by_name(self, response):
        """Browse by name"""
        # for href in response.xpath('//*[@class="bucket-list"]//@href'):
        #     yield Request(
        #         url=href.extract(),
        #         meta={'priority': 0},
        #         callback=self.parse_all_links)

        z_url = 'https://www.linkedin.com/directory/companies-z-100/'

        yield Request(
            url=z_url,
            callback=self.parse_all_links)

    def parse_all_links(self, response):
        hrefs = response.xpath('//*[@class="columns"]//@href').extract()
        childs = [get_dir(href) for href in hrefs]

        node = get_node(get_dir(response.url))
        update_childs(node, childs)

        # Current directory is a leaf
        if is_leaf(hrefs):
            item = LinkedinCrawlerItem()

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
