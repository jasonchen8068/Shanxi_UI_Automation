# -*- coding:utf-8 -*-

# from Connect_db import ConnectDb
# import re
# from time import sleep
# from Driver import Driver
# from Log_print import Log
# from Element_operation import Element
# from Login import Login
# from Call_api import MyRequest
# from Loan import Loan
# import sys
# from OpenAccount import OpenAccount
# reload(sys)
# sys.setdefaultencoding('utf-8')
# from MyAccountPage import AccountPage
import os
# b = Driver()
# d = b.browser_open("https://www.shsxsw.cn/")
#
# Log().info("testlog---------")
# c = ConnectDb("credit-online", "postgres", "123456", "10.7.106.245", "5432")
# c.Connect_to_postgreSQL()
# res = c.ExecuteSQL("select * from address where id = 6030767")
# #
# for i in res[0]:
#     print type(i), i
# c.Disconnect_from_postgreSQL()
# sleep(1)
# elem = Element(d)
# elem.click('class', 'loan-apply-btn')
# sleep(2)
# # elem.click('class')
# # elem.click('id', 'username')
# elem.text_input('id', 'username', "18252023049")
# sleep(1)
#
# b.browser_close()
# driver = Driver().browser_open("https://www.shsxsw.cn/login")
# res = Login(driver).login('18252023049', '123456')
# D = Driver()
# A = AccountPage(D, '18252023049', 'cjs123456')
# A.loanlist_page()
# D.browser_close()


# c = ConnectDb("SX_CREDIT_ONLINE_B", "postgres", "123456", "10.7.106.245", "5432")
# c.Connect_to_postgreSQL()
# res = c.ExecuteSQL(
#     "select send_content from credit_t_sms_message where mobile = '%s' ORDER BY created_date desc limit 1" % '18252023049')
# print res[0][0]
# parr = r'[0-9]{6}'
# rec = re.compile(parr)
# res = rec.findall(res[0][0])
# print res
# url = "http://p.3.cn/prices/mgets?skuIds=J_954086&type=1"
# para = {'skuIds':'J_954086', 'type':'1'}
# res = MyRequest.get(url)
# print res.text, res.status_code
# D = Driver()
# L = Loan(D, '18252023049', 'cjs123456')
# L.loan(u'善楼贷', u'等额本息', '6', '20000', u'扩大经营')

from selenium import webdriver
d = webdriver.Firefox()
d.get("http://www.baidu.com")
d.close()
# os.system('taskkill /F /IM geckodriver.exe')
d = webdriver.Firefox()
d.get("https://www.shsxsw.cn/")
d.close()