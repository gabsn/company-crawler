# coding: utf-8

from datetime import datetime, timedelta

from mongoengine import Document
from mongoengine import StringField, DateTimeField
from scrapy.http import Request
from scrapy.spiders import Spider

from crawler.items import CompaniesItem
from crawler.extractor import extract
from utils.mongodb import connect_mongoengine


X_RAW_DATA = '//code[@id="stream-right-rail-embed-id-content"]'


def get_links():
    return Links.objects(last_fetch_at__exists=False)


def get_last_fetch_at(url):
    now = datetime.now()
    Links.objects(url=url).update_one(set__last_fetch_at=now)
    return now


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
        raw_data = response.xpath(X_RAW_DATA)

        item = CompaniesItem()
        item['url'] = response.url
        item['last_fetch_at'] = get_last_fetch_at(response.url)
        item = extract(item, raw_data.extract_first())

        yield item
