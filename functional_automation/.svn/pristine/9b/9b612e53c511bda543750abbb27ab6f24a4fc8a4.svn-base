# -*- coding:utf-8 -*-
import sys
sys.path.append(r'E:\pythonworkspace\functional_automation\credit1.0\Automation\Driver')
sys.path.append(r'E:\pythonworkspace\functional_automation\credit1.0\Automation\Web\testcase\business_class')
sys.path.append(r'E:\pythonworkspace\functional_automation\credit1.0\Automation\Web\testcase\method')
from Driver import Driver
import unittest
from Loan import Loan

class TestLoan(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.D = Driver()

    def test008_loan(self):

        L = Loan(self.D, '18252023049', 'cjs123456')
        L.loan(u'善楼贷', u'等额本息', '6', '20000', u'扩大经营')

    def test009_loan(self):
        pass

    @classmethod
    def tearDownClass(cls):
        cls.D.browser_close()


if __name__ == '__main__':
    unittest.main()