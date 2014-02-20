#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
"""
import tornado.escape
from tornado import gen

from base_handler import BaseHandler

from lib.pyrestful import mediatypes
from lib.pyrestful.rest import get, post, put, delete

from common.web_conf import API_VERSION


# user CRUD
class UserResource(BaseHandler):


    @gen.coroutine
    @tornado.web.asynchronous
    @post(_path="/"+API_VERSION+"/users",  _produces=mediatypes.APPLICATION_JSON)
    def createUser(self):

        data = self.check_args()
        result = {}

        if not data.get("uid", None):
            self._gen_response(status_txt='uid should not be empty', log_message='track args bad arg data.')
            return

        result = yield self.db.add_user(uid=data["uid"])
        if not result.get('status_code', None):
            result['status_code'] = 200
            result['status_txt'] = 'OK'

        self.write(tornado.escape.json_encode(result))
        self.finish()
        return


    @gen.coroutine
    @tornado.web.asynchronous
    @post(_path="/"+API_VERSION+"/users/login", _produces=mediatypes.APPLICATION_JSON)
    def loginUser(self):


        data = self.check_args()
        result = {}

        if not data.get("uid", None):
            self._gen_response(status_txt='uid should not be empty', log_message='track args bad arg data.')
            return

        result = yield self.db.login_user(uid=data["uid"], pwd=None)

        self.write(tornado.escape.json_encode(result))
        self.finish()
        return


    @gen.coroutine
    @tornado.web.asynchronous
    @delete(_path="/"+API_VERSION+"/users/{uid}", types=[str], _produces=mediatypes.APPLICATION_JSON)
    def deleteUser(self, uid):

        result = yield self.db.del_user(uid=uid)

        self.write(tornado.escape.json_encode(result))
        self.finish()
        return
