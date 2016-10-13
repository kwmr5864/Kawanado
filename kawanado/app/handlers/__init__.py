import os
import tornado.web
from tornado import template


def make_app(debug=False):
    settings = {
        "static_path": os.path.join(os.path.dirname(__file__), "static"),
        "cookie_secret": "__TODO:_GENERATE_YOUR_OWN_RANDOM_VALUE_HERE__",
        "login_url": "/login",
        "xsrf_cookies": True,
        'debug': debug,
    }
    handlers = [
        (r"/", MainHandler),
        (r"/(apple-touch-icon\.png)", tornado.web.StaticFileHandler,
         dict(path=settings['static_path'])),
    ]
    return tornado.web.Application(handlers, **settings)


class MainHandler(tornado.web.RequestHandler):
    def data_received(self, chunk):
        pass

    def get(self):
        loader = template.Loader('/var/www/kawanado/app/templates')
        self.write(loader.load('index.html').generate(**{
            'title': 'tornado sample',
            'text': 'hello, tornado!',
        }))
