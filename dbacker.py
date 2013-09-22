#!/usr/bin/env python
# coding=utf-8

from dbacker import DBacker, providers

if __name__ == '__main__':
    backer = DBacker('pk0a9jwl410l0uf', 'zzhnwpar0pg66hy')
    if not backer.is_login():
        backer.login()
    backer.add_provider('sentry',
        providers.PostgresqlProvider('sentry', 'sentry', 'localhost', 8000, 'sentry'))
    backer.backup()