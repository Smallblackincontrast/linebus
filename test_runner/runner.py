# coding=utf-8
import time
import os
import unittest

from test_runner.html_test_runner import HTMLTestRunner


class TestRunner(object):
    def __init__(self, cases, title, description):
        self.cases = cases
        self.title = title
        self.des = description

    def run(self):
        now = time.strftime("%Y-%m-%d_%H_%M_%S")
        fp = open("./report/" + now + "_result.html", 'wb')
        tests = unittest.defaultTestLoader.discover(self.cases, pattern='test_*.py', top_level_dir=None)
        runner = HTMLTestRunner(stream=fp, title=self.title, description=self.des)
        runner.run(tests)
        fp.close()

    def debug(self):
        tests = unittest.defaultTestLoader.discover(self.cases, pattern='test_*.py', top_level_dir=None)
        runner = unittest.TextTestRunner(verbosity=2)
        runner.run(tests)


if __name__ == '__main__':
    TestRunner("../se_project", "测试报告", "测试执行情况").run()
    # TestRunner("../se_project", "测试报告", "测试执行情况").debug()
