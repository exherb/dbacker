#!/usr/bin/env python
# coding=utf-8

import os

from dbacker import DBacker, providers

from config import databases, dropbox

if __name__ == '__main__':
    backer = DBacker(os.path.dirname(__file__),
                     dropbox['key'], dropbox['sec'])
    if not backer.is_login():
        backer.login()

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
