#!/usr/bin/env python
# -*- coding:utf-8 -*-

from Infrastructure.Form.Forms import BaseForm
from Infrastructure.Form.Fields import StringField
from Infrastructure.Form.Fields import IntegerField




class RegisterForm(BaseForm):

    def __init__(self):
        self.username = StringField()
        self.password = StringField()
        self.email_code = StringField()

        super(RegisterForm, self).__init__()

class LoginForm(BaseForm):

    def __init__(self):
        self.username = StringField()
        self.passwd = StringField()
        self.code = StringField()

        super(LoginForm, self).__init__()