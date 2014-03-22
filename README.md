# WHAT
A api server demo based on tornado,motor,pyrestful.

# TODO
- type check
- Authentication
  - token
  - key
  - based on SSL
  - oauth
- authority
- multiple data type support
- rate limit
- api documents
- more features(ref the eve)

# DONE
- 2014.02.18 error handling，refer [d3status][1] for the view of api error(api server should not give errr status code,but just 200)
- rest urls

# Inspired ones
- [tornado-restful-handler-classes][http://stackoverflow.com/questions/8176185/tornado-restful-handler-classes]
- [what is a good api][www.vinaysahni.com/best-practices-for-a-pragmatic-restful-api#versioning]
- [what is a good api in chinese][http://xingrz.us/2013/2013-06-14/restful-api.html]
- [douban api][www.douban.com/service/apidoc/guide]
- [github api][http://developer.github.com/v3/]
- [how to design a good oauth server][http://tech.shift.com/post/39516330935/implementing-a-python-oauth-2-0-provider-part-1]
- slide
  - [基于flask的eve API框架，貌似很不错的样子][https://speakerdeck.com/nicola/developing-restful-web-apis-with-python-flask-and-mongodb]
  - [eve 框架介绍][https://speakerdeck.com/nicola/eve-rest-api-for-humans]

[1]: https://github.com/felinx/d3status
