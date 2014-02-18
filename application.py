#!/usr/bin/env python
# encoding: utf-8
import sys
from os.path import dirname
sys.path.insert(0,"./lib")

import tornado
from tornado.options import define, options

from api.server_handler import ServerResource
from api.user_handler import UserResource
from api.token_handler import TokenResource
from api.comm_handler import Better404

from common import web_log
from database import mongodb_asy

from lib import pyrestful

define("debug", default=True, help="debug mode")
define("f", default=None, help="config file")
define("port", default=8880, help="the port tornado listen to")
define("bind_ip", default="0.0.0.0", help="the bind ip")


class RestService(pyrestful.rest.RestService):
    def __init__(self):

        settings = dict(
            debug=options.debug,
            autoescape=None,
        )

        rest_handlers = [ServerResource, UserResource, TokenResource]

        norm_handlers = [(r"/.*",Better404)]
        # norm_handlers = []

        super(RestService, self).__init__(rest_handlers, handlers=norm_handlers, **settings)

        web_log.init()
        self.log = web_log.debugf("")

        self.db = mongodb_asy.Mongodb(log=self.log)

        self.log.debug("load finished! listening on %s:%s" % (options.bind_ip, options.port))

def main():
    tornado.options.parse_command_line()
    if options.f:
        tornado.options.parse_config_file(options.f)

    app = RestService()

    app.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":
  main()
