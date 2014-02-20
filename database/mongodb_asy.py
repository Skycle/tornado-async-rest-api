#! /usr/bin/env python
# -*- coding: utf-8 -*-

# from __future__ import unicode_literals
import motor
import pymongo
import tornado

import base64
import hashlib
import random

from common.web_conf import MONGO_SETTINGS


class Mongodb(object):
    def __init__(self, log=None):
        connection  = motor.MotorClient(MONGO_SETTINGS['mongo']['host'], MONGO_SETTINGS['mongo']['port'], max_pool_size=1000).open_sync()
        self.db = connection[MONGO_SETTINGS['mongo']['db']]
        self.log = log

    # #TODO better dup server error solutions
    # @tornado.gen.coroutine
    # def add_server(self, server_list=None) :
    #     result = {}
    #     try:
    #         # TODO for duplicate error
    #         yield motor.Op(self.db["server"].insert, [{'address': server} for server in server_list])
    #     except pymongo.errors.DuplicateKeyError:
    #         self.log.error('create server failed, duplicate server.')
    #         result.update({
    #             'status_code': 400,  # TODO better code?
    #             'status_txt': 'create server failed, duplicate server.'})
    #         raise tornado.gen.Return(result)

    #     raise tornado.gen.Return({})

    @tornado.gen.coroutine
    def add_server(self, address=None) :
        result = {}
        try:
            # FIXME can't be called on paral
            server_id_info = yield motor.Op(self.db["helpers"].find_and_modify,
                                       query={"server_id_current":{"$gt":0}},
                                       update={'$inc': {'server_id_current': 1}},
                                       # sort={'_id': pymongo.ASCENDING},
                                   )
            # yield motor.Op(self.db["server"].insert, {'address': server_id, 'id': server_id_info["server_id_current"]})
            yield motor.Op(self.db["server"].update, {'address':address }, {"$set":{'id':server_id_info["server_id_current"], "address": address}},upsert=True)

            raise tornado.gen.Return({'id': int(server_id_info['server_id_current'])})

        except pymongo.errors.DuplicateKeyError:
            self.log.error('create server failed, duplicate server.')
            result.update({
                'status_code': 400,  # TODO better code?
                'status_txt': 'create server failed, duplicate server.'})
            raise tornado.gen.Return(result)

    @tornado.gen.coroutine
    def del_server(self, server_list=None) :

        result = {}

        try:
            for server in server_list:
                result = yield motor.Op(self.db["server"].remove,
                                        {'id': int(server)})
        except Exception, e:
            err_msg= 'serious error: %s' % e
            self.log.error(err_msg)
            result.update({
                'status_code': 500,
                'status_txt': 'error unkown.may try latter'})
            raise tornado.gen.Return(result)

        raise tornado.gen.Return(None)

    @tornado.gen.coroutine
    def add_user(self, uid=None) :
        result = {}
        token = base64.b64encode(hashlib.sha256( str(random.getrandbits(256)) ).digest(), random.choice(['rA','aZ','gQ','hH','hG','aR','DD'])).rstrip('==')

        # TODO more error situation hanled
        try:
            yield motor.Op(self.db["user"].insert,
                           {'_id': uid, 'token': token})
        except pymongo.errors.DuplicateKeyError:
            err_msg = 'create user failed, duplicate user.'
            self.log.error(err_msg)
            result.update({
                'status_code': 400,
                'status_txt': err_msg})
            raise tornado.gen.Return(result)
        except Exception, e:
            err_msg= 'serious error: %s' % e
            self.log.error(err_msg)
            result.update({
                'status_code': 400,
                'status_txt': 'error unkown.may try latter'})
            raise tornado.gen.Return(result)

        raise tornado.gen.Return({'result':{'token':token}})

    @tornado.gen.coroutine
    def login_user(self, uid=None, pwd=None) :
        result = {}
        token = base64.b64encode(hashlib.sha256( str(random.getrandbits(256)) ).digest(), random.choice(['rA','aZ','gQ','hH','hG','aR','DD'])).rstrip('==')

        # TODO more error situation hanled
        try:
            yield motor.Op(self.db["user"].update,
                           {'_id': uid},
                           {"$set":{'token': token}},
                           upsert=True
            )
        except pymongo.errors.DuplicateKeyError:
            err_msg = 'create user failed, duplicate user.'
            self.log.error(err_msg)
            result.update({
                'status_code': 400,
                'status_txt': err_msg})
            raise tornado.gen.Return(result)
        except Exception, e:
            err_msg= 'serious error: %s' % e
            self.log.error(err_msg)
            result.update({
                'status_code': 400,
                'status_txt': 'error unkown.may try latter'})
            raise tornado.gen.Return(result)

        raise tornado.gen.Return({'result':{'token':token}})


    @tornado.gen.coroutine
    def del_user(self, uid=None) :

        # TODO what about unexit user del ??
        try:
            result = yield motor.Op(self.db["user"].remove,
                                    {'_id': uid})
        except Exception, e:
            err_msg= 'serious error: %s' % e
            self.log.error(err_msg)
            result.update({
                'status_code': 500,
                'status_txt': 'error unkown.may try latter'})
            raise tornado.gen.Return(result)

        raise tornado.gen.Return({})

    @tornado.gen.coroutine
    def validate_token(self, uid=None, token=None) :

        result = {}
        is_exit = yield motor.Op(self.db["user"].find_one,
                       # {'_id': uid, 'token': token})
                                 {'token': str(token)})
        if not is_exit:
            result = {'is_valid':0}
        else:
            result = {'is_valid':1}

        raise tornado.gen.Return(result)

    @tornado.gen.coroutine
    def distribute_user(self, uid=None):
        """
        distribute users to servers
        """
        result = {}

        cursor = self.db['server'].find().sort([('_id', -1)])

        server_list = yield motor.Op(cursor.to_list)

        if len(server_list) > 0:
            server = server_list[random.randrange(len(server_list))]
            result = {"address":server['address']}
        else:
            result.update({
                'status_code': 400,
                'status_txt': 'there is no address exit'
                })

        raise tornado.gen.Return(result)
