#!/usr/bin/env python
# -*- coding: utf-8 -*-
import libtwitter, sys, json, codecs, requests
def main():
    # useing utf-8 code
    sys.stdout = codecs.getwriter('utf_8')(sys.stdout)
    if len(sys.argv) == 1:
        c = 20
    elif len(sys.argv) == 2:
        c = sys.argv[1]
    else:
        print 'command line error'
        sys.exit(1)
    url = 'https://api.twitter.com/1.1/statuses/home_timeline.json'
    params = {'count': c}
    t = libtwitter.twiterclient(url, 'GET')
    req = t.send(params)
    if req == None:
        print 'error : req is None'
    timeLineData = json.loads(req.text, 'utf-8')
    for i in timeLineData:
        print '======================================================================'
        print unicode(i['user']['name']) + ' @' + unicode(i['user']['screen_name'])
        print unicode(i['text'])
        print 'id : ' + unicode(i['id_str'])
        # print str(i)
    print '======================================================================'

if __name__ == '__main__':
    main()
