#!/usr/bin/env python
# -*- coding:utf-8 -*-
import tornado.web
from ..Core.HttpRequest import AdminRequestHandler

class MainHandler(AdminRequestHandler):
    def get(self):
        self.write("Hello, world")