# coding: utf-8

import pdb
import multiprocessing
from billiard import Process

from time import sleep
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from twisted.internet import reactor

from crawler.spiders.companies import CompaniesSpider
from scrapy.crawler import CrawlerProcess
from utils.mongodb import connect_mongoengine
from crawler.mongo import Links

SETTINGS = get_project_settings()


class CompaniesCrawler(object):

    def __init__(self):
        self.crawler = CrawlerProcess(SETTINGS)

    def _crawl(self, spider):
        self.crawler.crawl(spider)
        self.crawler.start()
        self.crawler.stop()

    def crawl(self, spider):
        p = Process(
            target=self._crawl,
            args=[spider]
        )
        p.start()
        p.join()


if __name__ == "__main__":

    # Connect to dataBase
    connect_mongoengine()

    while (Links.to_crawl() > 3000):
        crawler = CompaniesCrawler()
        spider = CompaniesSpider()
        crawler.crawl(spider)
        sleep(5)
