#-*- coding:utf-8 -*-
from selenium import webdriver
import sys
sys.path.append(r'E:\pythonworkspace\functional_automation\credit1.0\Automation\Driver')
sys.path.append(r'E:\pythonworkspace\functional_automation\credit1.0\Automation\Web\testcase\business_class')
sys.path.append(r'E:\pythonworkspace\functional_automation\credit1.0\Automation\Web\testcase\method')
from Driver import Driver
from Login import Login
from Log_print import Log
import unittest



class TestLogin(unittest.TestCase):

    def setUp(self):
        self.D = Driver()
        self.driver = self.D.browser_open("http://10.7.106.235:8000/login")
        # self.log = Log()

    def test001_login(self):
        if Login(self.driver).login('18252023049', 'cjs123456'):
            Log.info("test001_login pass")

    def test002_login(self):
        if Login(self.driver).login('', '123456'):
            Log.info("test002_login pass")

    def test003_login(self):
        if Login(self.driver).login('18252023049', ''):
            Log.info("test003_login pass")

    def tearDown(self):
        self.D.browser_close()
        # os.system('taskkill /F /IM geckodriver.exe')


if __name__ == "__main__":
    unittest.main()
    # print sys.path