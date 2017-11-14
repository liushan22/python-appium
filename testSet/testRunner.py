# -*- coding: utf-8 -*-


import unittest

import common.report as report
from testApp.testSet.common.myServer import myServer
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
        self.ms = myServer()

    def run(self):
        self.ms.run()
        time.sleep(5)
        if self.ms.isServerStart():
            suite = unittest.TestSuite()
            # suite.addTest(testcase1("test_login"))
            suite.addTest(testcase2("test_passenger"))
            runner = createReport.getReportConfig()
            # runner = unittest.TextTestRunner(verbosity=2)
            runner.run(suite)
       # else:
           #  print "appium is not start"

    def driverquit(self):
        self.ms.quit()

if __name__ == '__main__':
    test = runTest()
    test.run()
    # test.driverquit()
    createReport.getfp().close()
    log = logger(report.today_report_path).getlog()
    log.info("test over")

