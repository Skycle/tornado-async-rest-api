#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
"""
import tornado
from tornado.web import HTTPError
from tornado import httputil

import pyrestful
import pyrestful.rest


class BaseHandler(pyrestful.rest.RestHandler):

    def send_error(self, status_code=500, **kwargs):
        """
        Generates the custom HTTP error.And always return 200 code.

        """
        reason = None
        if 'exc_info' in kwargs:
            exception = kwargs['exc_info'][1]
            if isinstance(exception, HTTPError) and exception.reason:
                reason = exception.reason
        try:
            msg = reason if reason else httputil.responses[status_code]
        except KeyError:
            msg = "unkown error"

        result = {"status_code":status_code, "reason": msg}

        self.clear()
        self.set_header("Content-Type", "application/json")
        self.set_status(200)
        self.write(tornado.escape.json_encode(result))
        self.finish()

    @property
    def db(self):
        return self.application.db

    @property
    def log(self):
        return self.application.log

    def check_args(self):
        d = None

        try:
            d = tornado.escape.json_decode(self.request.body)
        except ValueError, e:
            _ = 'decode track data error. e=%s' % e
            self._gen_response(status_txt='decode json error', log_message=_)
            return

        return d


    ### private help funcs
    def _gen_response(self, status_code=500, status_txt=None,log_message=None):
        r = {}
        self.log.error(log_message)
        r['status_code'] = status_code
        r['status_txt']  = status_txt

        self.write(tornado.escape.json_encode(r))
        self.finish()
