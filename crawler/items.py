# coding: utf-8

from scrapy import Item, Field


class LinksItem(Item):
    url = Field()


class CompaniesItem(Item):
    url = Field()
