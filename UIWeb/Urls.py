#!/usr/bin/env python
# -*- coding:utf-8 -*-

from .Controllers import Account
from .Controllers import Home

patterns = [
     (r"/Login.html$", Account.LoginHandler),
     (r"/CheckCode.html$", Account.CheckCodeHandler),
     (r"/Register.html$", Account.RegisterHandler),
     (r"/Index.html$", Home.IndexHandler),
     (r"/Detail-(?P<product_id>\d+)-(?P<price_id>\d+).html$", Home.DetailHandler),
     (r"/Pay.html$", Home.PayHandler),
     (r"/", Home.IndexHandler),
]