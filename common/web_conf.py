#! /usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import inspect, os

SITE_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe()))))
LOG_PATH = SITE_ROOT + "/log/"

MONGO_SETTINGS = {
    'mongo': {
       'host': '127.0.0.1',
       'port': 27017,
       'db': 'q1_account',
    },
}

FCGI_SETTIGNS = {
    'fcgi_port': 1024,
}

API_VERSION = 'v1'
