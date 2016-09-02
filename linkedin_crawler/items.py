# coding: utf-8

from scrapy import Item, Field


class LinkedinLinksItem(Item):
    url = Field()


class LinkedinCompaniesItem(Item):
    url = Field()
