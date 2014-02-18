#!/usr/bin/env python
# encoding: utf-8
import tornado.escape

from base_handler import BaseHandler

from lib.pyrestful import mediatypes
from lib.pyrestful.rest import get, post, put, delete


class Better404(BaseHandler):

    def _write_404(self):
        result = {"status_code":404, "reason":"method not exit at all...=("}
        self.write(tornado.escape.json_encode(result))
        self.finish()
        return

    def get(self):
        self._write_404()
