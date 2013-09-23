#!/usr/bin/env python
# coding=utf-8

import os

import dropbox

class DBacker(object):

    def __init__(self, base_dir, app_key, app_secret):
        super(DBacker, self).__init__()
        self.providers = {}
        self.token_file = os.path.join(base_dir, '.dropbox')

        self.app_key = app_key
        self.app_secret = app_secret

        self.api_client = None
        try:
            token = open(self.token_file).read()
            self.api_client = dropbox.client.DropboxClient(token)
        except IOError:
            pass

    def add_provider(self, name, provider):
        if name in self.providers:
            raise RuntimeError('{0} already exists'.format(name))
        self.providers[name] = provider

    def is_login(self):
        return self.api_client != None

    def login(self):
        flow = dropbox.client.DropboxOAuth2FlowNoRedirect(self.app_key, self.app_secret)
        authorize_url = flow.start()
        print(u'前往 ' + authorize_url + u' 认证\n')
        code = raw_input(u'请输入授权码: '.encode('utf-8')).strip()

        try:
            access_token, user_id = flow.finish(code)
        except dropbox.rest.ErrorResponse, e:
            raise e

        with open(self.token_file, 'w') as f:
            f.write(access_token)
        self.api_client = dropbox.client.DropboxClient(access_token)

    def backup(self):
        for provider_name, provider in self.providers.iteritems():
            print('backuping {0} with {1}...'.format(provider_name, str(provider.__class__.__name__)))
            file_path = provider.backup()
            try:
                self.api_client.put_file('/' + provider_name, open(file_path, 'rb'), overwrite = True)
            finally:
                os.remove(file_path)
        print('backup complete.')

