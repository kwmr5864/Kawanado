import tornado.ioloop
import tornado.web
import tornado.httpserver

from handlers import make_app

if __name__ == "__main__":
    app = make_app()
    server = tornado.httpserver.HTTPServer(app)
    server.bind(8000)
    server.bind(8001)
    server.bind(8002)
    server.bind(8003)
    server.start(0)
    tornado.ioloop.IOLoop.current().start()
