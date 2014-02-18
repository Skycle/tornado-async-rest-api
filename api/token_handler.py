#!/usr/bin/env python
# encoding: utf-8

import tornado.escape
from tornado import gen

from base_handler import BaseHandler

from lib.pyrestful import mediatypes
from lib.pyrestful.rest import get, post, put, delete

from common.web_conf import API_VERSION

class TokenResource(BaseHandler):

    @gen.coroutine
    @tornado.web.asynchronous
    @get(_path="/"+API_VERSION+"/token/{token_id}", _produces=mediatypes.APPLICATION_JSON)
    def validate_token(self, token=None):

        result = yield self.db.validate_token(token=token)

        self.write(tornado.escape.json_encode(result))
        self.finish()

        return
