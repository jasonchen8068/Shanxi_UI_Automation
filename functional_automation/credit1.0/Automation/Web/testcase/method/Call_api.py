#HTTP request
# -*- coding:utf-8 -*-
import requests
from Log_print import Log

class MyRequest(object):

    @classmethod
    def get(cls, url='', headers='', cookies=''):
        if url == '':
            Log.warn("call get() error:url is null")
        else:
            sess = requests.Session()
            if headers == '':
                if cookies == '':
                    res = sess.get(url)
                else:
                    res = sess.get(url, cookies = cookies)
            else:
                if cookies == '':
                    res = sess.get(url, headers = headers)
                else:
                    res = sess.get(url, headers = headers, cookies = cookies)

        return res


    @classmethod
    def post(cls, url='', data='', headers='', cookies=''):
        if url == '':
            Log.warn("call post() error:url is null")
        else:
            sess = requests.Session()
            if headers == '':
                if cookies == '':
                    res = sess.post(url, data=data)
                else:
                    res = sess.get(url, data=data, cookies=cookies)
            else:
                if cookies == '':
                    res = sess.get(url, data=data, headers=headers)
                else:
                    res = sess.get(url, data=data, headers=headers, cookies=cookies)

        return res



