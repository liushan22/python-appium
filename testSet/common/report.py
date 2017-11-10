# -*- coding: utf-8 -*-
import HTMLTestRunner
import time
import os
parent_path=os.path.abspath(os.path.dirname(os.path.realpath(__file__))+os.path.sep+"..")
report_path = os.path.join(os.path.dirname(parent_path), 'result')
today_report_path = ""
print report_path
import sys
reload(sys)
sys.setdefaultencoding('utf8')


class report:
    def __init__(self):
        self.runner = ""
        self.fp = ""
        self.sendReport()

    def sendReport(self):
        global today_report_path
        now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
        today = time.strftime("%Y%m%d", time.localtime(time.time()))
        today_report_path = report_path + "\\" + today
        if not os.path.isdir(today_report_path):
            os.mkdir(today_report_path)
        report_abspath = os.path.join(today_report_path, now + '_report.html')
        self.fp = open(report_abspath, 'wb')
        self.runner = HTMLTestRunner.HTMLTestRunner(stream=self.fp, title="appium自动测试报告", description="用例执行结果：")

    def getReportConfig(self):
        return self.runner

    def getfp(self):
        return self.fp

if __name__ == "__main__":
    re = report()
    re.sendReport()