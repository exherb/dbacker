#!/usr/bin/env python
# coding=utf-8

import os

from dbacker import DBacker, providers

from config import databases

if __name__ == '__main__':
    backer = DBacker(os.path.dirname(__file__), 'pk0a9jwl410l0uf', 'zzhnwpar0pg66hy')
    if not backer.is_login():
        backer.login()

    providers.Provider.get_provider('postgresql')

    for name, database in databases.iteritems():
        provider_name = database['provider']
        provider_cls = providers.Provider.get_provider(provider_name)
        provider = provider_cls(database.get('user', None),
            database.get('password', None),
            database.get('database', None),
            database.get('host', None),
            database.get('port', None),
            )
        backer.add_provider(name, provider)

    backer.backup()
