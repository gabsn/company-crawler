# coding: utf-8

from datetime import datetime, timedelta

from mongoengine import Document
from mongoengine import StringField, DateTimeField
from scrapy.http import Request
from scrapy.spiders import Spider

from crawler.items import CompaniesItem
from crawler.extractor import extract
from utils.mongodb import connect_mongoengine


def get_links():
    return Links.objects(last_fetch_at__exists=False)


def get_last_fetch_at(url):
    try:
        last_fetch_at = Links.objects(url=url).first().last_fetch_at
    except:
        update_last_fetch_at(url)
        last_fetch_at = datetime.now()

    return last_fetch_at


def update_last_fetch_at(url):
    Links.objects(url=url).update_one(set__last_fetch_at=datetime.now())


class Links(Document):
    meta = {'collection': 'linkedin_links'}
    url = StringField()
    last_fetch_at = DateTimeField(default=datetime.min)


class CompaniesSpider(Spider):
    name = "Companies"
    collection = "linkedin_companies"
    start_urls = ['https://www.linkedin.com']

    def __init__(self):
        super(CompaniesSpider, self).__init__()
        connect_mongoengine()

    def parse(self, response):
        """First request needed to get cookies"""
        for link in Links.objects():
            if datetime.now() - link.last_fetch_at > timedelta(days=7):
                yield Request(
                    url=link.url,
                    callback=self.parse_company)

    def parse_company(self, response):
        update_last_fetch_at(response.url)

        item = CompaniesItem()
        item['url'] = response.url
        item['last_fetch_at'] = get_last_fetch_at(response.url)

        raw_data = response.xpath(
            '//code[@id="stream-right-rail-embed-id-content"]')
        if raw_data:
            yield extract(item, raw_data[0].extract())
