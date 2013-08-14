__author__ = 'brightwang'

import sys
from tornado.options import define, options
from tornado.wsgi import WSGIContainer
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from mysite import app
from tornado.options import define, options


define("port", default=8888, help="run on the given port", type=int)

options.parse_command_line()
print(options.port)
http_server = HTTPServer(WSGIContainer(app))
http_server.listen(options.port)
IOLoop.instance().start()
