import tornado.ioloop

from handlers import make_app

if __name__ == "__main__":
    app = make_app(True)
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
