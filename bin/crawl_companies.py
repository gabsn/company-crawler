# coding: utf-8

from time import sleep
from multiprocessing import Process, active_children

from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

from crawler.mongo import Links
from crawler.spiders.companies import CompaniesSpider
from utils.mongodb import connect_mongoengine

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

    while (Links.to_crawl() > 0):
        crawler = CompaniesCrawler()
        crawler.crawl(CompaniesSpider())

        while active_children():
            sleep(2)
