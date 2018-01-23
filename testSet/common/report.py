# -*- coding: utf-8 -*-
import HTMLTestRunner
import time
import os
import testSet.util.date as date


class report:
    def __init__(self):
        self.runner = ""
        self.fp = ""
        self.sendReport()

    def sendReport(self):
        now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
        if not os.path.isdir(date.today_report_path):
            os.mkdir(date.today_report_path)
        report_abspath = os.path.join(date.today_report_path, now + '_report.html')
        self.fp = open(report_abspath, 'wb')
        self.runner = HTMLTestRunner.HTMLTestRunner(
            stream=self.fp, title="appium自动化测试报告", description="用例执行结果：")

    def getReportConfig(self):
        return self.runner

    def getfp(self):
        return self.fp

if __name__ == "__main__":
    re = report()
    re.sendReport()