# element operation class
# -*- coding:utf-8 -*-
from Log_print import Log
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys


class Element(object):

    def __init__(self, driver):
        self._driver = driver

    def click(self, method='id', path=''):
        if path == '':
            Log.warn("call click() error : The path is null")
            raise ValueError

        else:
            if method == 'id':
                elem = self._driver.find_element_by_id(path)
                elem.click()

            if method == 'name':
                elem = self._driver.find_element_by_name(path)
                elem.click()

            if method == 'class':
                elem = self._driver.find_element_by_class_name(path)
                elem.click()

            if method == 'xpath':
                elem = self._driver.find_element_by_xpath(path)
                elem.click()

            if method == 'css':
                elem = self._driver.find_element_by_css(path)
                elem.click()

            if method == 'linktext':
                elem = self._driver.find_element_by_link_text(path)
                elem.click()

    def text_input(self, method='id', path='', key=""):
        if path == '':
            Log.warn("call text_input() error : The path is null")
            raise ValueError

        else:
            if method == 'id':
                elem = self._driver.find_element_by_id(path)
                elem.clear()
                elem.send_keys(key)

            if method == 'name':
                elem = self._driver.find_element_by_name(path)
                elem.clear()
                elem.send_keys(key)

            if method == 'class':
                elem = self._driver.find_element_by_class_name(path)
                elem.clear()
                elem.send_keys(key)

            if method == 'xpath':
                elem = self._driver.find_element_by_xpath(path)
                elem.clear()
                elem.send_keys(key)

            if method == 'css':
                elem = self._driver.find_element_by_css(path)
                elem.clear()
                elem.send_keys(key)

    def text_input_noclear(self, method='id', path='', key=""):
        if path == '':
            Log.warn("call text_input() error : The path is null")
            raise ValueError

        else:
            if method == 'id':
                elem = self._driver.find_element_by_id(path)
                # elem.clear()
                elem.send_keys(key)

            if method == 'name':
                elem = self._driver.find_element_by_name(path)
                # elem.clear()
                elem.send_keys(key)

            if method == 'class':
                elem = self._driver.find_element_by_class_name(path)
                # elem.clear()
                elem.send_keys(key)

            if method == 'xpath':
                elem = self._driver.find_element_by_xpath(path)
                # elem.clear()
                elem.send_keys(key)

            if method == 'css':
                elem = self._driver.find_element_by_css(path)
                # elem.clear()
                elem.send_keys(key)

    def get_elem_text(self, method='id', path=''):

        if method == 'id':
            return self._driver.find_element_by_id(path).text

        if method == 'class':
            return self._driver.find_element_by_class(path).text

        if method == 'xpath':
            return self._driver.find_element_by_xpath(path).text

    def get_current_url(self):

        return self._driver.current_url

    def dropdown_choose(self, method='index', value=0, elemmethod='id', elempath=''):

        if method == 'index' and elemmethod == 'id':
            Select(self._driver.find_element_by_id(elempath)).select_by_index(value)

        if method == 'value' and elemmethod == 'id':
            Select(self._driver.find_element_by_id(elempath)).select_by_value(value)

        if method == 'value' and elemmethod == 'xpath':
            Select(self._driver.find_element_by_xpath(elempath)).select_by_value(value)

        if method == 'text' and elemmethod == 'xpath':
            Select(self._driver.find_element_by_xpath(elempath)).select_by_visible_text(value)

    def enter(self, method='id', path=''):
        if path == '':
            Log.warn("call enter() error : The path is null")
            raise ValueError

        else:
            if method == 'id':
                elem = self._driver.find_element_by_id(path)
                elem.send_keys(Keys.ENTER)

            if method == 'name':
                elem = self._driver.find_element_by_name(path)
                elem.clear()
                elem.send_keys(Keys.ENTER)

            if method == 'class':
                elem = self._driver.find_element_by_class_name(path)
                elem.clear()
                elem.send_keys(Keys.ENTER)

            if method == 'xpath':
                elem = self._driver.find_element_by_xpath(path)
                elem.clear()
                elem.send_keys(Keys.ENTER)

            if method == 'css':
                elem = self._driver.find_element_by_css(path)
                elem.clear()
                elem.send_keys(Keys.ENTER)

    def get_elem_shuxingzhi(self, method = 'id', path = '', shuxing = ''):

        if path == '' or shuxing == '':
            Log.warn("call get_elem_shuxingzhi() error : The path is null")
            raise ValueError

        else:
            if method == 'id':
                elem = self._driver.find_element_by_id(path)
                return elem.get_attribute(shuxing)

            if method == 'name':
                elem = self._driver.find_element_by_name(path)
                return elem.get_attribute(shuxing)

            if method == 'class':
                elem = self._driver.find_element_by_class_name(path)
                return elem.get_attribute(shuxing)

            if method == 'xpath':
                elem = self._driver.find_element_by_xpath(path)
                return elem.get_attribute(shuxing)



