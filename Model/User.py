#!/usr/bin/env python
# -*- coding:utf-8 -*-

class IUserRepository:

    pass


class UserService:

    def __init__(self, user_repository):
        self.userRepository = user_repository

    def get_user_to_select(self):

        user_list = self.userRepository.fetch_user()

        return user_list

    def login_user_by_pwd(self,username,passwd):
        login = self.userRepository.login_user_by_pwd(username,passwd)
        return login
