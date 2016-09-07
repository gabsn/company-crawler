# coding: utf-8

import random
import pdb
from time import sleep
from billiard import Process

from scrapy.downloadermiddlewares.useragent import UserAgentMiddleware
from scrapy.utils.response import response_status_message
from scrapy.exceptions import CloseSpider
from scrapy.utils.test import get_crawler
from scrapy.spiders import Spider
from scrapy.crawler import *
from scrapy.utils.project import get_project_settings
from scrapy.settings import Settings

from twisted.internet import reactor
from scrapy.utils.log import configure_logging


from crawler.data.useragents import USER_AGENTS
from crawler.spiders.companies import CompaniesSpider

class UrlCrawlerScript(Process):
    def __init__(self, spider):
        Process.__init__(self)
        self.crawler = CrawlerRunner()
        self.crawler.crawl(spider)  

    def run(self):
        d = self.crawler.join()
        d.addBoth(lambda _: reactor.stop())       
        #reactor.run(0)

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
            self.crawler.engine.close_spider(spider, reason)

            #crawler = UrlCrawlerScript(CompaniesSpider)
            #crawler.start()

            #crawler = Crawler(CompaniesSpider, settings)
            #crawler.crawl()

        return response


class RotateUserAgentMiddleware(UserAgentMiddleware):
    """Set a User-Agent at each request"""

    def __init__(self, user_agent=''):
        self.user_agent = user_agent

    def process_request(self, request, spider):
        user_agent = random.choice(USER_AGENTS)
        request.headers.setdefault('User-Agent', user_agent)
