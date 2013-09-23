#!/usr/bin/env python
# coding=utf-8

import os

from dbacker.providers import Provider

class MongodbProvider(Provider):

    def __init__(self, user, password,
        database,
        host = None, port = None):
        if host == None:
            host = 'localhost'
        if port == None:
            port = 27017
        super(MongodbProvider, self).__init__(user, password, database, host, port)

    def gen_backup_cmd(self, tmp_file_path):
        os.remove(tmp_file_path)
        os.mkdir(tmp_file_path)
        if self.user != None and self.password != None:
            cmd = 'mongodump -h {0} --port {1} -u {2} -p {3} -d {4} -o {5}'.format(self.host, self.port,
                self.user, self.password,
                self.database,
                tmp_file_path)
        else:
            cmd = 'mongodump -h {0} --port {1} -d {2} -o {3}'.format(self.host, self.port,
                self.database,
                tmp_file_path)
        return tmp_file_path, cmd

