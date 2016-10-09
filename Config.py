#!/usr/bin/env python
# -*- coding:utf-8 -*-

routes = (
    {
        'host_pattern': 'www.zhangyanlin.com',
        'route_path': 'UIWeb.Urls',
        'route_name': 'patterns'
    },
    {
        'host_pattern': 'admin.zhangyanlin.com',
        'route_path': 'UIAdmin.Urls',
        'route_name': 'patterns'},
    {
        'host_pattern': 'dealer.zhangyanlin.com',
        'route_path': 'UIDealer.Urls',
        'route_name': 'patterns'
    }
)


ui_method = (
    'Infrastructure.UIMethods.Null',
)

ui_module = (
    'Infrastructure.UIModules.Null',
)

settings = {
    'template_path': 'Views',
    'static_path': 'Statics',
    'static_url_prefix': '/Statics/',
}

PY_MYSQL_CONN_DICT = {
    "host": '127.0.0.1',
    "port": 3306,
    "user": 'root',
    "passwd": '',
    "db": 'ShoppingDb',
    "charset": 'utf8'
}