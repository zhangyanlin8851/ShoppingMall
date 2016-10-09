#!/usr/bin/env python
# -*- coding:utf-8 -*-
import tornado.web
from ..Core.HttpRequest import AdminRequestHandler

class IndexHandler(AdminRequestHandler):
    def get(self):
        # 调用协调者

        self.render('Home/Index.html')