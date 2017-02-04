#!/usr/bin/env python
# -*- coding: utf-8 -*-
import libtwitter, sys
def main(argc, args):
    if argc != 2:
        print 'comannd line error'
        sys.exit(1)

    url = "https://api.twitter.com/1.1/statuses/update.json"
    # ツイート本文
    params = {'status': args[1]}
    t = libtwitter.twiterclient(url,'POST')
    req = t.send(params)
    if req.status_code == 200:
        print 'Success!'
    else:
        print 'Failure!'

if __name__ == '__main__':
    main(len(sys.argv), sys.argv)
