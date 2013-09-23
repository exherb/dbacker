#!/usr/bin/env python
# coding=utf-8

import os
import tempfile
import shutil
import imp

from contextlib import closing
from zipfile import ZipFile, ZIP_DEFLATED

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

    @classmethod
    def get_provider(cls, database_name):
        providers = imp.load_source('providers', os.path.join(os.path.dirname(__file__), '{0}_provider.py'.format(database_name)))
        return getattr(providers, '{0}Provider'.format(database_name.title()))

    def gen_backup_cmd(self, tmp_file_path):
        pass

    def backup(self):
        tmp_file, tmp_file_path = tempfile.mkstemp('.dbacker')
        try:
            tmp_file_path, cmd = self.gen_backup_cmd(tmp_file_path)
            if os.system(cmd) != 0:
                raise RuntimeError('backup command line fail')
            if os.path.isdir(tmp_file_path):
                try:
                    tmp_file, ziped_tmp_file_path = tempfile.mkstemp('.dbacker')
                    with closing(ZipFile(ziped_tmp_file_path, "w", ZIP_DEFLATED)) as tmp_zip_file:
                        for root, dirs, file_paths in os.walk(tmp_file_path):
                            for file_path in file_paths:
                                abs_file_path = os.path.join(root, file_path)
                                zip_file_path = abs_file_path[len(tmp_file_path)+len(os.sep):]
                                tmp_zip_file.write(abs_file_path, zip_file_path)

                finally:
                    shutil.rmtree(tmp_file_path)
                tmp_file_path = ziped_tmp_file_path
        except Exception, e:
            if os.path.isdir(tmp_file_path):
                shutil.rmtree(tmp_file_path)
            else:
                os.remove(tmp_file_path)
            raise e

        return tmp_file_path
