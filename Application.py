#!/usr/bin/env python
# -*- coding:utf-8 -*-
import tornado.ioloop
import tornado.web
import Config


def load_ui_module(settings):
    module_list = []
    for path in Config.ui_method:
        m = __import__(path, fromlist=True)
        module_list.append(m)
    settings['ui_modules'] = module_list


def load_ui_method(settings):
    method_list = []
    for path in Config.ui_method:
        m = __import__(path, fromlist=True)
        method_list.append(m)
    settings['ui_methods'] = method_list


def load_routes(app):
    for route in Config.routes:
        host_pattern = route['host_pattern']
        route_path = route['route_path']
        route_name = route['route_name']

        m = __import__(route_path, fromlist=True)
        pattern_list = getattr(m, route_name)

        app.add_handlers(host_pattern, pattern_list)


def load_hook():
    pass


def start():

    settings = {}

    load_ui_method(settings)
    load_ui_module(settings)

    settings.update(Config.settings)

    application = tornado.web.Application([
        #(r"/index", home.IndexHandler),
    ], **settings)

    load_routes(application)

    load_hook()
    print('http://127.0.0.1:8888')

    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":
    start()

