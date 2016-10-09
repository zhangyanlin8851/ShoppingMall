#!/usr/bin/env python
# -*- coding:utf-8 -*-
from tornado.web import UIModule
from tornado import escape


class NullModule(UIModule):

    def render(self, *args, **kwargs):
        return escape.xhtml_escape('<h1>wupeiqi</h1>')