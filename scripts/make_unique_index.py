#! /usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from random import randint
import json
import urllib2

import pymongo
from pymongo import MongoClient, DESCENDING, ASCENDING


MONGO_SETTINGS = {
    'mongo': {
       'host': '127.0.0.1',
       'port': 27017,
       'db': 'q1_account',
    },
}

client = MongoClient(host=MONGO_SETTINGS['mongo']['host'], port=MONGO_SETTINGS['mongo']['port'])

if __name__ == '__main__':

    db = client[MONGO_SETTINGS['mongo']['db']]
    server_coll = db['server']

    res = server_coll.ensure_index("address",unique=True)
    print res
    #db.eval('db.server.ensureIndex({ "address":1},{"unique":true})')
