#!/usr/bin/env python
# coding=utf-8

class Provider(object):

    def __init__(self, user, password,
        database,
        host, port):
        super(Provider, self).__init__()
        self.user = user
        self.password = password
        self.host = host
        self.port = port
        self.database = database

    def backup(self):
        pass

