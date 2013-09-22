#!/usr/bin/env python
# coding=utf-8

import dropbox

class DBacker(object):

    def __init__(self, app_key, app_secret):
        super(DBacker, self).__init__()
        self.providers = {}
        self.token_file = '.dropbox'

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
            file_path = provider.backup()
            self.api_client.put_file('/' + provider_name, open(file_path, 'rb'), overwrite = True)
