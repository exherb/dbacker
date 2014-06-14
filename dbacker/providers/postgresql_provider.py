#!/usr/bin/env python
# coding=utf-8

import os

from dbacker.providers import Provider


class PostgresqlProvider(Provider):

    def __init__(self, user, password,
                 database,
                 host=None, port=None):
        if not host:
            host = 'localhost'
        if not port:
            port = 5432
        super(PostgresqlProvider, self).__init__(user, password, database,
                                                 host, port)

    def gen_backup_cmd(self, tmp_file_path):
        os.environ['PGPASSWORD'] = self.password
        cmd = 'pg_dump -h {0} -p {1} -U {2} {3} > {4}'.\
            format(self.host, self.port,
                   self.user,
                   self.database,
                   tmp_file_path)
        return tmp_file_path, cmd
