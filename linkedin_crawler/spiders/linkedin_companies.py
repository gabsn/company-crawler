# coding: utf-8

import pdb
import json

from scrapy.http import Request
from scrapy.spiders import Spider

from linkedin_crawler.items import LinkedinCompaniesItem
from linkedin_crawler.settings import SETTINGS_PATH


def get_company_links():
    links = json.load(open(join(SETTINGS_PATH, 'data/linkedin_links.json')))
    return links


class LinkedinCompaniesSpider(Spider):
    name = "LinkedinCompaniesSpider"
    collection = "linkedin_companies"
    start_urls = ['https://www.linkedin.com']

    def parse(self, response):
        """First request needed to get cookies"""
        links = get_company_links()
        pdb.set_trace()

        yield Request(
            url='',
            callback=self.parse_by_name)
