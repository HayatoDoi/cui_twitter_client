#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os, sys, json, codecs, requests
from requests_oauthlib import OAuth1
def main():
    # useing utf-8 code
    sys.stdout = codecs.getwriter('utf_8')(sys.stdout)
    if len(sys.argv) != 1:
        print 'command line error'
        sys.exit(1)
    profilejson = open(os.environ.get('HOME') + '/.tconf.json','r')
    profile = json.load(profilejson)
    print str(profile)
    CK = profile['CK']
    CS = profile['CS']
    AT = profile['AT']
    AS = profile['AS']
    profilejson.close()
    print CK
    print CS
    print AT
    print AS

    url = 'https://api.twitter.com/1.1/statuses/home_timeline.json'
    auth = OAuth1(CK, CS, AT, AS)
    req = requests.post(url, auth=auth, stream=True, data={"follow":"no_______nonono"})
    for i in req.iter_lines():
        print unicode(i)
    #     print '======================================================================'
    #     print unicode(i['user']['name']) + ' @' + unicode(i['user']['screen_name'])
    #     print unicode(i['text'])
    #     print 'id : ' + unicode(i['id_str'])
    #     # print str(i)
    # print '======================================================================'

if __name__ == '__main__':
    main()
