# -*- coding: utf-8 -*-


import unittest

import common.report as report
from common.myServer import myServer
from test_01 import test_01 as testcase1
from test_02 import test_02 as testcase2

createReport = report.report()
import os
import sys
import time
from common.log import logger
reload(sys)
sys.setdefaultencoding('utf8')


class runTest():
    def __init__(self):
        pass

    def run(self):
        ms = myServer()
        ms.run()
        time.sleep(5)
        # driver = ms.isServerStart()
        # if driver:
        suite = unittest.TestSuite()
        # self.getDriver(driver)
        # suite.addTest(testcase1("test_login"))
        suite.addTest(testcase2("test_passenger"))
        runner = createReport.getReportConfig()
        # runner = unittest.TextTestRunner(verbosity=2)
        runner.run(suite)
        ms.quit()
       # else:
           #  print "appium is not start"

    def getDriver(self, driver):
        return driver

if __name__ == '__main__':
    test = runTest()
    test.run()
    # test.driverquit()
    createReport.getfp().close()
    log = logger(report.today_report_path).getlog()
    log.info("test over")

