# coding: utf-8

import pdb
import json
from datetime import datetime, timedelta
from os.path import join

from mongoengine import Document
from mongoengine import StringField, DateTimeField
from scrapy.http import Request
from scrapy.spiders import Spider

from crawler.items import CompaniesItem
from crawler.settings import SETTINGS_PATH
from utils.mongodb import connect_mongoengine


def get_company_links():
    links = []
    with open(join(SETTINGS_PATH, 'data/linkedin_links.json')) as f_links:
        for line in f_links:
            links.append(json.loads(line)['url'])
    return links


def get_links():
    return Links.objects(last_fetch_at__exists=False)


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
        yield item

