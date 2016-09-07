# coding: utf-8

import random
import pdb
from time import sleep

from scrapy.downloadermiddlewares.useragent import UserAgentMiddleware
from scrapy.utils.response import response_status_message
from scrapy.exceptions import CloseSpider
from scrapy.utils.test import get_crawler
from scrapy.spiders import Spider
from scrapy.crawler import *
from scrapy.utils.project import get_project_settings
from scrapy.settings import Settings



from crawler.data.useragents import USER_AGENTS
from crawler.spiders.companies import CompaniesSpider


class StatusHandlerMiddleware(object):
    """Close spider when encounters 999 status code"""

    def __init__(self, crawler):
        self.crawler = crawler

    @classmethod
    def from_crawler(cls, crawler):
        return cls(crawler)

    def process_response(self, request, response, spider):
        if response.status in [999] and spider.running:
            reason = "Received 999 status code"
            spider.running = False

            self.crawler.engine.close_spider(spider, reason)
            sleep(2)
            settings = get_project_settings()
            crawler = Crawler(CompaniesSpider, settings)
            crawler.crawl()

        return response
            #runner = CrawlerRunner()
            #runner.crawl(CompaniesSpider)
        #new_spider = CompaniesSpider()
        #new_crawler = create_crawler(new_spider)
        #new_crawler.engine.open_spider(new_spider)

        #return response


class RotateUserAgentMiddleware(UserAgentMiddleware):
    """Set a User-Agent at each request"""

    def __init__(self, user_agent=''):
        self.user_agent = user_agent

    def process_request(self, request, spider):
        user_agent = random.choice(USER_AGENTS)
        request.headers.setdefault('User-Agent', user_agent)
