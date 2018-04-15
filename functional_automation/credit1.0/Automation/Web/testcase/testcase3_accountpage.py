# -*- coding:utf-8 -*-
import sys
sys.path.append(r'E:\pythonworkspace\functional_automation\credit1.0\Automation\Driver')
sys.path.append(r'E:\pythonworkspace\functional_automation\credit1.0\Automation\Web\testcase\business_class')
sys.path.append(r'E:\pythonworkspace\functional_automation\credit1.0\Automation\Web\testcase\method')
from Driver import Driver
import unittest
from MyAccountPage import AccountPage
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


class TestAccountPage(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.D = Driver()
        cls.A = AccountPage(cls.D, '18252023049', 'cjs123456')

    def test005_accountpage_baseinfo(self):
        self.A.base_info_edit()

    def test006_accountpage_contactinfo(self):
        self.A.contact_Info_edit()

    def test007_accountpage_loanlist(self):
        self.A.loanlist_page()

    @classmethod
    def tearDownClass(cls):
        cls.D.browser_close()


if __name__ == '__main__':
    unittest.main()
