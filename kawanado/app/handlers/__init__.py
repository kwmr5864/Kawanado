import os
import tornado.web

from abc import ABCMeta
from tornado import template


def make_app(debug=False):
    settings = {
        "static_path": "%s/../static" % os.path.join(os.path.dirname(__file__)),
        "cookie_secret": "__TODO:_GENERATE_YOUR_OWN_RANDOM_VALUE_HERE__",
        "login_url": "/login",
        "xsrf_cookies": True,
        'debug': debug,
    }
    handlers = [
        (r"/", MainHandler),
        (r"/search", SearchHandler),
        (r"/(apple-touch-icon\.png)", tornado.web.StaticFileHandler,
         dict(path=settings['static_path'])),
    ]
    return tornado.web.Application(handlers, **settings)


class AbstractHandler(tornado.web.RequestHandler):
    """
    抽象ハンドラ。
    """
    __metaclass__ = ABCMeta

    def data_received(self, chunk):
        pass

    def view(self, template_name, params):
        """
        画面を表示する。
        :param str template_name: テンプレート名
        :param dict params: パラメータ
        :return:
        """
        if not params.get('keyword'):
            params['keyword'] = ''

        loader = template.Loader("%s/../templates" % os.path.dirname(os.path.abspath(__file__)))
        self.write(loader.load("%s.html" % template_name).generate(**params))


class MainHandler(AbstractHandler):
    def get(self):
        self.view('index', {
            'title': 'Top',
        })


class SearchHandler(AbstractHandler):
    def get(self):
        keyword = self.get_argument('keyword', '')

        self.view('search', {
            'title': "Search Result: %s" % keyword,
            'keyword': keyword,
        })
