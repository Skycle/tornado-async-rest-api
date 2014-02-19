q1账号系统接口说明
=============

# version
 - 版本：1.0
 - 请在每个请求url前面加 /v1。比如注册server，url应为 /v1/servers

# request
- server
    - POST
        - url: '/servers'
        - format: json
        - request: {"server":'127.0.0.1:80'}
        - response:
            - success:  {"id":2}
            - fail:     {"status_code": 400, "status_txt": "create server failed, duplicate server."}

    - GET
       - url: '/servers'
       - request: none
       - response:
            - success: {"address": "127.0.0.1:8880"}
            - fail: {"status_code": 400, "status_txt": "there is no address exit"}

    - PUT
    - PATCH
    - DELETE
        - url: '/server/{sever_id}'
        - request:  none
        - response:
            - success: HTTP 200
            - fail: {"status_code": 500, 'status_txt': 'error unkown.may try latter'}

- User
    - POST
        - url:  '/users'
        - format: json
        - request: {'uid':'12312312312312', 'pwd':'2318231231'}
        - response:
            - success: {"token": "kBZ6b4osZf2ens9Aa1PKDZozpVWkROD97q4leV4rMdw"}
            - fail:    {"status_code": 500, "status_txt": "create user failed, duplicate user."}
    - GET
    - PUT/PATCH
    - DELETE
        - url:  '/users/{uid}'
        - request: none
        - response:
            - success: HTTP 200
            - fail: {"status_code": 500, 'status_txt': 'error unkown.may try latter'}

- User validate
    - GET
    - url:  '/token/{token}'
    - request: none
    - response:
        - valid: {"is_valid": 1}
        - not valid: {"is_valid": 0}

# error
- 访问不存在的方法
  - {"status_code": 404, "reason": "method not exit at all...=("}
- 访问方法不允许
  - {"status_code": 405, "reason": "Method Not Allowed"}
- 系统出错
  - {"status_code": 500, "reason": "Internal Server Error : %s"%detail)
