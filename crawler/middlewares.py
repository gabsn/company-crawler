# coding: utf-8

import random

from scrapy.downloadermiddlewares.useragent import UserAgentMiddleware

from crawler.data.useragents import USER_AGENTS


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

        return response


class RotateUserAgentMiddleware(UserAgentMiddleware):
    """Set a User-Agent at each request"""

    def __init__(self, user_agent=''):
        super(RotateUserAgentMiddleware, self).__init__()
        self.user_agent = user_agent

    def process_request(self, request, spider):
        user_agent = random.choice(USER_AGENTS)
        request.headers.setdefault('User-Agent', user_agent)
