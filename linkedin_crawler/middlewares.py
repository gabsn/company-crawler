# coding: utf-8

import random
import logging

from scrapy.downloadermiddlewares.useragent import UserAgentMiddleware

from linkedin_crawler.useragents import USER_AGENTS


def display_user_agent(request):
    logging.debug(u'User-Agent: {}'
                  .format(request.headers.get('User-Agent')))


class RotateUserAgentMiddleware(UserAgentMiddleware):
    """Set a User-Agent at each request"""

    def __init__(self, user_agent=''):
        self.user_agent = user_agent

    def process_request(self, request, spider):
        user_agent = random.choice(USER_AGENTS)
        request.headers.setdefault('User-Agent', user_agent)
