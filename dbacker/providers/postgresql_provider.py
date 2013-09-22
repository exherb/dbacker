#!/usr/bin/env python
# coding=utf-8

from . import Provider

class PostgresqlProvider(Provider):

    def __init__(self, user, password,
        database,
        host = 'localhost', port = 5432):
        super(PostgresqlProvider, self).__init__(user, password, database, host, port)

    def backup(self):
        pass

