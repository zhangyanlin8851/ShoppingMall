#!/usr/bin/env python
# -*- coding:utf-8 -*-
import json
from datetime import date
from datetime import datetime
from decimal import Decimal


class JsonCustomEncoder(json.JSONEncoder):

    def default(self, field):

        if isinstance(field, datetime):
            return field.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(field, date):
            return field.strftime('%Y-%m-%d')
        elif isinstance(field, Decimal):
            return str(field)
        else:
            return json.JSONEncoder.default(self, field)
