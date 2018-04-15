# -*- coding:utf-8 -*-
import sys
sys.path.append(r'E:\pythonworkspace\functional_automation\credit1.0\Automation\Driver')
sys.path.append(r'E:\pythonworkspace\functional_automation\credit1.0\Automation\Web\testcase\business_class')
sys.path.append(r'E:\pythonworkspace\functional_automation\credit1.0\Automation\Web\testcase\method')
from Driver import Driver
import unittest
from OpenAccount import OpenAccount


class TestOpenAccount(unittest.TestCase):

    def setUp(self):
        self.D = Driver()
        self.driver = self.D.browser_open("http://10.7.106.235:8000/login")
        self.oa = OpenAccount(self.driver)

    def test004_openaccount(self):
        # self.oa.open_account('18252023049', 'cjs123456', u'陈进松', '320621199301178313', '6214852116479075',
        #                      '18051969073')
        # 该账户已开通了
        # self.oa.open_account('18252023050', 'cjs123456', u'陈进松', '320621199301178313', '6214852116479075',
        #                      '18051969073')
        pass

    def tearDown(self):
        self.D.browser_close()


if __name__ == "__main__":
    unittest.main()
