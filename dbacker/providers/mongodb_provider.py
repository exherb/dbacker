#!/usr/bin/env python
# coding=utf-8

from . import Provider

class MongodbProvider(Provider):

    def __init__(self, user, password,
        database,
        host = 'localhost', port = 27017):
        super(MongodbProvider, self).__init__(user, password, database, host, port)

    def backup(self):
        pass

