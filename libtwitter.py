#!/usr/bin/env python
# -*- coding: utf-8 -*-
from requests_oauthlib import OAuth1Session
import requests,sys,os,json
class twiterclient:
    def __init__(self, url, method):
        self.url = url
        self.method = method
        jsonPath = os.environ.get('HOME') + '/.tconf.json'
        jsonData = open(jsonPath,'r')
        config = json.load(jsonData)
        self.CK = config['CK']
        self.CS = config['CS']
        self.AT = config['AT']
        self.AS = config['AS']
        jsonData.close()

    def send(self, params):
        client = OAuth1Session(self.CK, self.CS, self.AT, self.AS)
        if self.method == 'POST':
            req = client.post(self.url, params = params)
        elif self.method == 'GET':
            req = client.get(self.url, params = params)
        else:
            print 'method error'
            return None
        if req.status_code == 200:
            return req
        else:
            print 'error : status code: ' + str(req.status_code)
            return None
