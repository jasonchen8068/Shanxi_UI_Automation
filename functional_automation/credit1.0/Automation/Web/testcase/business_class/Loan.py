# loan
# -*- coding:utf-8 -*-
from Log_print import Log
from Element_operation import Element
from time import sleep
from Login import Login
import os
# import sys
# reload(sys)
# sys.setdefaultencoding('utf-8')


class Loan(object):

    def __init__(self, D, username, password):
        self._D = D
        self._driver = self._D.browser_open("http://10.7.106.235:8000/login")
        self._elem = Element(self._driver)
        Login(self._driver).login(username, password)

    # 申请借款
    def loan(self, loan_type, repay_method, loan_term, loan_amount, loan_purpose, invitation_code=''):

        #step 1
        # 取消审核中的借款
        self._elem.click('linktext', u'我的借款')
        sleep(2)
        try:
            if self._elem.get_elem_text('xpath',
                                        ".//*[@id='base_info_body']/div/div[2]/div/table[1]/tbody/tr[3]/td[6]") == u'审核中':
                self._elem.click('xpath', ".//*[@id='base_info_body']/div/div[2]/div/table[1]/tbody/tr[3]/td[7]/a/font")
                sleep(3)
                self._elem.click('xpath', "//a[@id='qx_loanApplybut']")
                sleep(1)
            elif self._elem.get_elem_text('xpath',
                                          ".//*[@id='base_info_body']/div/div[2]/div/table[1]/tbody/tr[3]/td[6]") == u'申请':
                self._elem.click('xpath',
                                 ".//*[@id='base_info_body']/div/div[2]/div/table[1]/tbody/tr[3]/td[7]/a[2]/font")
                sleep(3)
                self._elem.click('xpath', "//a[@id='qx_loanApplybut']")
                sleep(1)

        except:

            Log.info(u'没有未结束的借款')

        finally:
            self._elem.click('linktext', u'我要借款')
            sleep(2)
            self._elem.click('xpath', 'html/body/div[1]/div[1]/div[1]/div/a')
            sleep(3)

            dict1 = {u'善薪贷': '51a7fa647e18641fe053326410ac9559', u'善美贷': '51a7fa647e36641fe053326410ac9559',
                     u'善楼贷': '51a7fa647e1d641fe053326410ac9559', u'善时贷': '51a7fa647e31641fe053326410ac9559',
                     u'保单贷': '51a7fa647e2c641fe053326410ac9559', u'学历贷': '51a7fa647e27641fe053326410ac9559',
                     u'精英贷': '51a7fa647e22641fe053326410ac9559', u'培训贷': '2c91808a5c901d6f015cab18708e087a'}

            for key, value in dict1.items():
                if key == loan_type:
                    self._elem.dropdown_choose('value', value, 'id', 'loan_product')

            self._elem.dropdown_choose('value', repay_method, 'id', 'loan_repayment_method')

            sleep(1)

            self._elem.dropdown_choose('value', loan_term, 'id', 'loan_term')

            self._elem.text_input('id', 'loan_amount', loan_amount)

            self._elem.dropdown_choose('value', loan_purpose, 'id', 'loan_purpose')

            self._elem.text_input('id', 'invitation_code', invitation_code)

            # self._elem.dropdown_choose('value', "001001001001005", 'id', 'loan_city')
            #
            # sleep(1)

            self._elem.click('id', "select2-loan_city-container")

            self._elem.text_input('class', 'select2-search__field', u'上海市')

            self._elem.enter('class', 'select2-search__field')

            self._elem.dropdown_choose('value', "5193c7186b38600de053326410acda90", 'id', 'loan_sales_department')

            sleep(1)


            self._elem.text_input('xpath', ".//*[@id='loanDesc']", u'善薪贷')

            self._elem.click('xpath',".//*[@id='loan_apply_btn']")

            sleep(3)

            #step 2
            # 身份证明
            self._elem.click('id', 'idcard_upload_btn')
            sleep(2)
            # upload three id pictures
            self._elem.click('xpath', "//div[@id='batchContainer']/button[@class='addFile add-file']")
            sleep(2)
            os.system(r"E:\pythonworkspace\functional_automation\autoit\loan_id_pic_upload.exe")
            sleep(1)
            self._elem.click('xpath', "//div[@id='batchContainer']/button[@class='addFile add-file']")
            sleep(2)
            os.system(r"E:\pythonworkspace\functional_automation\autoit\loan_id_pic_upload2.exe")
            sleep(1)
            self._elem.click('xpath', "//div[@id='batchContainer']/button[@class='addFile add-file']")
            sleep(2)
            os.system(r"E:\pythonworkspace\functional_automation\autoit\loan_id_pic_upload3.exe")
            sleep(1)

            self._elem.click('xpath', "//div[@id='batchContainer']/button[@class='batchUpload batch-upload']")
            sleep(2)
            self._elem.click('xpath', "//img[@src='/images/shade-closebtn.png']")
            sleep(1)

            # 房产证明
            self._elem.click('id', 'house_upload_btn')
            sleep(2)
            self._elem.click('xpath', "//div[@id='batchContainer']/button[@class='addFile add-file']")
            sleep(2)
            os.system(r"E:\pythonworkspace\functional_automation\autoit\loan_house_pic_upload.exe")
            sleep(1)
            self._elem.click('xpath', "//div[@id='batchContainer']/button[@class='batchUpload batch-upload']")
            sleep(2)
            self._elem.click('xpath', "//img[@src='/images/shade-closebtn.png']")
            sleep(1)

            # 居住证明
            self._elem.click('id', 'live_upload_btn')
            sleep(2)
            self._elem.click('xpath', "//div[@id='batchContainer']/button[@class='addFile add-file']")
            sleep(2)
            os.system(r"E:\pythonworkspace\functional_automation\autoit\loan_live_pic_upload.exe")
            sleep(1)
            self._elem.click('xpath', "//div[@id='batchContainer']/button[@class='batchUpload batch-upload']")
            sleep(2)
            self._elem.click('xpath', "//img[@src='/images/shade-closebtn.png']")
            sleep(1)

            # 我已阅读
            self._elem.click('id', 'loan_authorization_ipt')

            # 提交
            self._elem.click('id', 'loan_commit_btn')
            sleep(1)
            self._elem.click('id', 'confirm_commit_loan')
            sleep(1)

            # 断言提交成功页面
            assert self._elem.get_elem_text('xpath', "//h2[@style='color:#21aa71;']") == u'借款申请成功，请等待处理'







