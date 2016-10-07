# coding: utf-8

from mongoengine import connect

from crawler.settings import MONGODB


def connect_mongoengine():
    connect(
        db=MONGODB['db'],
        host=MONGODB['host'],
        port=MONGODB['port'],
    )
