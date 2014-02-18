#!/usr/bin/env python
# encoding: utf-8
import httplib
import json

# test case add_server
data = {"event": "add_server", "data":{"servers": ['127.0.0.4:80','128.12.3.1:90']}}

# test case del_server
# data = {"event": "del_server", "data":{"servers": ['127.0.0.2:80','128.12.3.1:90']}}

# test case add_user
# data = {"event": "add_user", "data":{"uid":"1234"}}

# TODO test case del_user
# data = {"event": "del_user", "data":{"uid":"1234"}}

# TODO validate user
data = {"event": "val_user", "data":{"uid":"1234", "token": 'kpwhupVCL0bQrRRqHtsDC3RasL832uPMmwlxLqfy0nA'}}
# data = {"event": "val_user", "data":{"uid":"234", "token": 'kpwhupVCL0bQrRRqHtsDC3RasL832uPMmwlxLqfy0nA'}}

headers = {"Content-type": "application/json", "Accept": "text/plain"}
conn = httplib.HTTPConnection('127.0.0.1',8880)
# conn.request("POST", "/api/server", json.dumps(data), headers)
conn.request("POST", "/api/user", json.dumps(data), headers)

r1 = conn.getresponse()
print r1.status, r1.reason

data1 = r1.read()
print data1
