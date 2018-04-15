# -*- coding:utf-8 -*-

import sys
import unittest
import os
import HTMLTestRunner
import time
import shutil


# 默认编码改为utf-8
reload(sys)
sys.setdefaultencoding('utf8')

# 用例路径
# case_path = os.path.join(os.getcwd())
case_path = r"E:\pythonworkspace\functional_automation\credit1.0\Automation\Web\testcase"


report_path1 = case_path.split(r'\testcase')[0]
# 报告存放路劲
report_path = os.path.join(report_path1, 'testreport')


def all_case():
    discover = unittest.defaultTestLoader.discover(case_path, pattern="test*.py", top_level_dir=None)
    return discover


if __name__ == "__main__":
    # 获取当前时间
    now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
    # 定义报告文件路劲和名称
    # report_abspath = os.path.join(report_path, "report_" + now + ".html")
    report_abspath = os.path.join(report_path, "report" + ".html")
    # 打开文件，将result写入
    fp = open(report_abspath, "wb")
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u'web自动化测试报告结果：', description=u'用例执行情况')
    runner.run(all_case())
    fp.close()

    # 移动报告
    oldname = "E:\\pythonworkspace\\functional_automation\\credit1.0\\Automation\\Web\\testreport\\" + "report.html"
    newname = "E:\\jenkins\\workspace\\automation_credit\\HTMLReport\\" + "report.html"
    shutil.copyfile(oldname, newname)
