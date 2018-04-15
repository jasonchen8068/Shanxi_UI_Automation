# login class
# -*- coding:utf-8 -*-
from Log_print import Log
from Element_operation import Element
from unittest import TestCase
from time import sleep
from Login import Login
from Connect_db import ConnectDb
import re


class OpenAccount(object):

    def __init__(self, driver):
        self._driver = driver
        self._elem = Element(self._driver)

    def open_account(self, username, password, name, ID, cardnumber, mphone):

        try:
            Login(self._driver).login(username, password)
        except Exception:
            Log.exception('login failed leads open account failed')
            raise

        self._elem.click('linktext', u'立即开通')
        sleep(2)
        self._elem.text_input('id', 'name', name)
        sleep(1)
        self._elem.text_input('id', 'idnum', ID)
        sleep(1)
        # dropdown operation
        self._elem.click('id', "select2-bankCode-container")
        sleep(1)
        self._elem.text_input('class', 'select2-search__field', u'招商银行')
        sleep(1)
        self._elem.enter('class', 'select2-search__field')
        sleep(1)
        self._elem.text_input('id', 'bankAccount', cardnumber)
        sleep(1)
        self._elem.text_input('id', 'mphone', mphone)
        sleep(1)
        # send message
        self._elem.click('id', "update_account_sendOldMobileVerificationCode_btn")
        sleep(3)
        # find sms code
        c = ConnectDb("SX_CREDIT_ONLINE_B", "postgres", "123456", "10.7.106.245", "5432")
        c.Connect_to_postgreSQL()
        res = c.ExecuteSQL(
            "select send_content from credit_t_sms_message where mobile = '%s' ORDER BY created_date desc limit 1" % username)
        c.Disconnect_from_postgreSQL()
        patt = r'[0-9]{6}'
        rec = re.compile(patt)
        res = rec.findall(res[0][0])
        self._elem.text_input('id', 'verification_code', res[0])
        # commit
        self._elem.click('id', "open_account_submit")
        # assert
