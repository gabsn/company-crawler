# coding: utf-8

import pdb
from mongoengine import Document
from mongoengine.fields import StringField, DateTimeField
from datetime import datetime


class Links(Document):
    meta = {'collection': 'linkedin_links'}
    url = StringField()
    last_fetch_at = DateTimeField(default=datetime.min)

    @staticmethod
    def to_crawl():
        return Links.objects(last_fetch_at__exists=False).count()
