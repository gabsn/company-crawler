# coding: utf-8

from scrapy import Item, Field


class LinksItem(Item):
    url = Field()


class CompaniesItem(Item):
    url = Field()
    last_fetch_at = Field()
    company_name = Field()
    company_type = Field()
    size = Field()
    description = Field()
    year_founded = Field()
    industry = Field()
    headquarters = Field()
    specialties = Field()
    website = Field()
    square_logo = Field()
    job_count = Field()
