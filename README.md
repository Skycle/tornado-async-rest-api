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
- [tornado-restful-handler-classes][2]
- [what is a good api][3]
- [what is a good api in chinese][4]
- [douban api][5]
- [github api][6]
- [how to design a good oauth server][7]
- slide
  - [基于flask的eve API框架，貌似很不错的样子][8]
  - [eve 框架介绍][9]

[1]: https://github.com/felinx/d3status
[2]: http://stackoverflow.com/questions/8176185/tornado-restful-handler-classes
[3]: www.vinaysahni.com/best-practices-for-a-pragmatic-restful-api#versioning
[4]: http://xingrz.us/2013/2013-06-14/restful-api.html
[5]: www.douban.com/service/apidoc/guide
[6]: http://developer.github.com/v3/
[7]: http://tech.shift.com/post/39516330935/implementing-a-python-oauth-2-0-provider-part-1
[8]: https://speakerdeck.com/nicola/developing-restful-web-apis-with-python-flask-and-mongodb
[9]: https://speakerdeck.com/nicola/eve-rest-api-for-humans
