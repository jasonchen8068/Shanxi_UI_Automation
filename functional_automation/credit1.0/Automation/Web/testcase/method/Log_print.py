# logging
# -*- coding:utf-8 -*-

import logging
import os


class Log(object):

    @classmethod
    def set_logger(cls):
        cls._logger = logging.getLogger()
        cls._logger.setLevel(level=logging.INFO)
        # path = os.getcwd()
        path = r"E:\pythonworkspace\functional_automation\credit1.0\Automation\Web\testcase"
        path = path.split(r'\testcase')[0]
        path = os.path.join(path, r"testreport\\")
        logpath = ''.join([path, "log.txt"])
        cls._handler = logging.FileHandler(logpath)
        cls._handler.setLevel(logging.INFO)
        formatt = logging.Formatter('%(asctime)s  - %(levelname)s - %(message)s')
        cls._handler.setFormatter(formatt)
        cls._logger.addHandler(cls._handler)

    @classmethod
    def info(cls, message):
        Log.set_logger()
        cls()._logger.info(message)
        cls()._logger.removeHandler(cls()._handler)

    @classmethod
    def warn(cls, message):
        Log.set_logger()
        cls()._logger.warn(message)
        cls()._logger.removeHandler(cls()._handler)

    @classmethod
    def debug(cls, message):
        Log.set_logger()
        cls()._logger.debug(message)
        cls()._logger.removeHandler(cls()._handler)

    @classmethod
    def exception(cls, message):
        Log.set_logger()
        cls()._logger.exception(message)
        cls()._logger.removeHandler(cls()._handler)
