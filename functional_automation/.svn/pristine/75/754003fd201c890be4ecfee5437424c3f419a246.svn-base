# -*- coding:utf-8 -*-
from Log_print import Log
from Element_operation import Element
from time import sleep
from Login import Login
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class AccountPage():

    def __init__(self, D, username, password):
        self._D = D
        self._driver = self._D.browser_open("http://10.7.106.235:8000/login")
        self._elem = Element(self._driver)
        Login(self._driver).login(username, password)
        # 未开户用户关掉弹框
        # self._elem.click('xpath', ".//*[@id='base_please_open_acc']/div[2]/div[1]/img")

    def base_info_edit(self):

        self._elem.click('linktext', u'我的借款')
        sleep(2)
        try:
            if self._elem.get_elem_text('xpath', ".//*[@id='base_info_body']/div/div[2]/div/table[1]/tbody/tr[3]/td[6]") == u'审核中':
                self._elem.click('xpath', ".//*[@id='base_info_body']/div/div[2]/div/table[1]/tbody/tr[3]/td[7]/a/font")
                sleep(3)
                self._elem.click('xpath', "//a[@id='qx_loanApplybut']")
                sleep(1)
            elif self._elem.get_elem_text('xpath', ".//*[@id='base_info_body']/div/div[2]/div/table[1]/tbody/tr[3]/td[6]") == u'申请':
                self._elem.click('xpath', ".//*[@id='base_info_body']/div/div[2]/div/table[1]/tbody/tr[3]/td[7]/a[2]/font")
                sleep(3)
                self._elem.click('xpath', "//a[@id='qx_loanApplybut']")
                sleep(1)

        except:

            Log.info(u'没有未结束的借款')

        finally:

            self._elem.click('linktext', u'基本信息')
            sleep(2)
            assert self._elem.get_current_url() == "http://10.7.106.235:8000/account/baseInfo"

            self._elem.click('xpath',"//button[@class='account-edit-btn ']")
            sleep(2)
            self._elem.dropdown_choose('value', u'本科', 'id', 'education')
            # sleep(1)
            self._elem.dropdown_choose('value', u'未婚', 'id', 'marriage')
            # sleep(1)
            self._elem.dropdown_choose('value', '110', 'id', 'live_province')
            # sleep(1)
            self._elem.dropdown_choose('value', '110100000000', 'id', 'live_city')
            # sleep(1)
            self._elem.dropdown_choose('value', '110101000000', 'id', 'live_county')
            # sleep(1)
            self._elem.text_input('name', 'liveDetailAddress', u'朝阳门南大街')
            # sleep(1)
            self._elem.text_input('name', 'workCompany', u'上海市腾讯大厦')
            # sleep(1)
            self._elem.text_input('name', 'cTel', '021-8857623')
            # sleep(1)
            self._elem.dropdown_choose('value', '310', 'id', 'company_province')
            # sleep(1)
            self._elem.dropdown_choose('value', '310100000000', 'id', 'company_city')
            # sleep(1)
            self._elem.dropdown_choose('value', '310104000000', 'id', 'company_county')
            # sleep(1)
            self._elem.text_input('name', 'companyDetailAddress', u'虹梅路1801号')
            # sleep(1)
            self._elem.text_input('name', 'workYears', '10')
            # sleep(1)
            self._elem.dropdown_choose('value', u'网银', 'id', 'pay_type')
            # sleep(1)
            self._elem.click('id', 'person_save_btn')
            sleep(2)
            # print self._elem.get_elem_text('xpath', ".//*[@id='edit_form']/div[4]/div[5]/div[2]/em")
            assert self._elem.get_elem_text('xpath', ".//*[@id='edit_form']/div[4]/div[5]/div[2]/em") == '10'

    def contact_Info_edit(self):
        self._elem.click('linktext', u'联系人信息')
        sleep(1)
        assert self._driver.current_url == "http://10.7.106.235:8000/account/contactInfo"
        self._elem.click('xpath', "//button[@id='contact_edit_btn']")

        self._elem.dropdown_choose('value', u'父母', 'id', 'contact_relation0')
        # sleep(1)
        self._elem.dropdown_choose('value', u'配偶', 'id', 'contact_relation1')
        # sleep(1)
        self._elem.dropdown_choose('value', u'朋友', 'id', 'contact_relation2')
        # sleep(1)
        self._elem.text_input('id', 'contact_name0', u'陈先生')
        self._elem.text_input('id', 'contact_name1', u'蒋先生')
        self._elem.text_input('id', 'contact_name2', u'吉先生')

        self._elem.text_input('id', 'contact_mphone0', '18011111111')
        self._elem.text_input('id', 'contact_mphone1', '18022222222')
        self._elem.text_input('id', 'contact_mphone2', '18033333333')

        self._elem.text_input('id', 'contact_tel0', '021-8811111')
        self._elem.text_input('id', 'contact_tel1', '021-8811112')
        self._elem.text_input('id', 'contact_tel2', '021-8811113')

        self._elem.click('name', 'contacts[0].isKnowLoanStr')
        #commit
        self._elem.click('xpath', ".//*[@id='contacts_save_btn']")
        sleep(1)

        #校验固定电话值
        assert self._elem.get_elem_shuxingzhi('id', 'contact_tel0', 'value') == '021-8811111'

    def loanlist_page(self):

        self._elem.click('linktext', u'我的借款')
        sleep(1)
        assert self._elem.get_current_url() == "http://10.7.106.235:8000/account/loanList"
        # test cancer loan








