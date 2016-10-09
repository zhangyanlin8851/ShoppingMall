#!/usr/bin/env python
# -*- coding:utf-8 -*-
import io
from Infrastructure import CheckCode
from ..Core.HttpRequest import WebRequestHandler
from UIWeb.forms.account import LoginForm
from Infrastructure.Core.HttpRequest import BaseRequestHandler
from Model.User import UserService
from Repository.UserRepository import UserRepository


class CheckCodeHandler(WebRequestHandler,BaseRequestHandler):
    def get(self, *args, **kwargs):
        stream = io.BytesIO()
        img, code = CheckCode.create_validate_code()
        img.save(stream, "png")
        self.session["CheckCode"] = code
        self.write(stream.getvalue())


class LoginHandler(WebRequestHandler,BaseRequestHandler):

    def get(self, *args, **kwargs):
        self.render('Account/Login.html',error = "")

    def post(self, *args, **kwargs):
        ret = {'status':True,'message':None,'data':None}
        form = LoginForm()
        if form.valid(self):
            login_service = UserService(UserRepository())
            login = login_service.login_user_by_pwd(form._value_dict['username'],form._value_dict['passwd'])

            if self.session['CheckCode'].lower() != form._value_dict['code'].lower():
                ret['status'] = False
                ret['message'] = "验证码错误"
                self.render('./account/login.html', error=ret['message'])
                return
            if not login:
                ret['status'] = False
                ret['message'] = '用户名密码错误'
                self.render('./account/login.html', error=ret['message'])
                return
            else:
                self.session["is_login"] = True
                self.redirect('/Pay.html')
                return




class LogoutHandler(WebRequestHandler):

    def get(self, *args, **kwargs):

        self.redirect('/Login.html')


class RegisterHandler(WebRequestHandler):

    def get(self, *args, **kwargs):
        self.render('Account/Register.html')










