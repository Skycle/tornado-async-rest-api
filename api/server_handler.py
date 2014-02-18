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

class ServerResource(BaseHandler):

    @gen.coroutine
    @tornado.web.asynchronous
    @post(_path="/"+API_VERSION+"/servers",  _produces=mediatypes.APPLICATION_JSON)
    def createServers(self):

        data = self.check_args()

        if not data.get("servers", None) or not isinstance(data["servers"], list):
            self._gen_response(status_txt='bad arg data', log_message='track args bad arg data.')
            return

        result = yield self.db.add_server(server_list=data["servers"])

        self.write(tornado.escape.json_encode(result))
        self.finish()
        return

    @gen.coroutine
    @tornado.web.asynchronous
    @delete(_path="/"+API_VERSION+"/servers/{server_id}", types=[str], _produces=mediatypes.APPLICATION_JSON)
    def deleteServer(self, server_id):

        result = yield self.db.del_server(server_list=[server_id])

        self.write(tornado.escape.json_encode(result))
        self.finish()
        return

    @gen.coroutine
    @tornado.web.asynchronous
    @get(_path="/"+API_VERSION+"/servers", _produces=mediatypes.APPLICATION_JSON)
    def distributeUser(self):

        result = yield self.db.distribute_user()

        self.write(tornado.escape.json_encode(result))
        self.finish()

        return
