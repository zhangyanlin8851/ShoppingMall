#!/usr/bin/env python
# -*- coding:utf-8 -*-
from Infrastructure.Form.Forms import BaseForm
from Infrastructure.Form.Fields import StringField
from Infrastructure.Form.Fields import IntegerField
from Infrastructure.Form.Fields import DecimalField


class JdProductForm(BaseForm):

    def __init__(self):

        self.title = StringField()
        self.img = StringField()
        self.img_list = StringField(required=False)
        self.detail_list = StringField(required=False)

        super(JdProductForm, self).__init__()


class JdProductPriceForm(BaseForm):

    def __init__(self):

        self.nid = StringField(required=False)
        self.product_id = IntegerField()
        self.standard = StringField()
        self.price = DecimalField()
        self.selling_price = DecimalField()

        super(JdProductPriceForm, self).__init__()
