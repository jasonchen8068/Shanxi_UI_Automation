# login class
# -*- coding:utf-8 -*-
from Log_print import Log
from Element_operation import Element
from unittest import TestCase
from time import sleep


class Login(TestCase):

    def __init__(self, driver):
        self._driver = driver
        # self.log = Log()

    def login(self, username, password):

        elem = Element(self._driver)
        elem.text_input('id', 'username', username)
        #sleep(1)
        elem.text_input('id', 'password', password)
        #sleep(2)
        elem.click('id', 'login_btn')
        sleep(3)
        if username == '':

            Log.info("username is null")
            try:
                assert u"请输入手机号" == elem.get_elem_text('id', 'username-error')
                flag = True

            except AssertionError:
                Log.exception('login'+'-%s-%s' % (username, password))
                raise

        elif password == '':
            Log.info("password is null")

            try:
                assert u"请输入密码" == elem.get_elem_text('id', 'password-error')
                flag = True
            except AssertionError:
                Log.exception('login' + '-%s-%s' % (username, password))
                raise

        else:
            try:
                assert elem.get_current_url() == 'http://10.7.106.235:8000/account'
                flag = True
            except AssertionError:
                Log.exception('login' + '-%s-%s' % (username, password))
                raise

        return flag
