#!/usr/bin/env python
# -*- coding:utf-8 -*-

from Model.User import IUserRepository
from Repository.DbConnection import DbConnection

class UserRepository(IUserRepository):

    def __init__(self):
        self.db_conn = DbConnection()

    def fetch_user(self):
        cursor = self.db_conn.connect()
        sql = """select nid as value,username as text from userinfo"""
        cursor.execute(sql)
        db_result = cursor.fetchall()
        self.db_conn.close()
        return db_result

    def login_user_by_pwd(self,username,passwd):
        cursor = self.db_conn.connect()
        sql = """select nid,username,email,last_login,vip,user_type from UserInfo where username=%s and password=%s"""
        cursor.execute(sql, (username, passwd))
        db_result = cursor.fetchone()
        self.db_conn.close()
        return db_result