# coding: utf-8

import pdb
import json

from os.path import join
from scrapy.http import Request
from scrapy.spiders import Spider

from linkedin_crawler.items import LinkedinCompaniesItem
from linkedin_crawler.settings import SETTINGS_PATH


def get_company_links():
    links = []
    with open(join(SETTINGS_PATH, 'data/linkedin_links.json')) as f_links:
        for line in f_links:
            links.append(json.loads(line)['url'])
    return links


class LinkedinCompaniesSpider(Spider):
    name = "LinkedinCompaniesSpider"
    collection = "linkedin_companies"
    start_urls = ['https://www.linkedin.com']

    def parse(self, response):
        """First request needed to get cookies"""
        self.links = get_company_links()

        while (self.links):
            yield Request(
                url=self.links[0],
                callback=self.parse_company)

            self.links.pop(0)

    def parse_company(self, response):
        item = LinkedinCompaniesItem()
        item['url'] = response.url
        yield item
