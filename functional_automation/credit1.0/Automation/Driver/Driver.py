# browser drive
# -*- coding:utf-8 -*-
from selenium import webdriver


class Driver(object):

    def __init__(self):
        self._browser = webdriver.Firefox()

    def browser_open(self, url):
        # driver.set_window_size(500, 500)
        self._browser.get(url)

        return self._browser

    def browser_close(self):
        self._browser.quit()

# if __name__ == "__main__":
#     driver = browser("http://www.shsxsw.cn")
