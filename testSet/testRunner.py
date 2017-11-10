# -*- coding: utf-8 -*-


from myServer import myServer
from test_01 import test_01 as testcase
import unittest
from common.report import report
createReport = report()
import os
import sys
reload(sys)
sys.setdefaultencoding('utf8')


class runTest():
    def __init__(self):
        pass

    def run(self):

        ms = myServer()
        ms.run()
        # if ms.isServerStart():
        # ms.quit()
        suite = unittest.TestSuite()
        suite.addTest(testcase("test_login"))
        runner = createReport.getReportConfig()
        # runner = unittest.TextTestRunner(verbosity=2)
        runner.run(suite)
        ms.quit()
       # else:
           #  print "appium is not start"

if __name__ == '__main__':
    test = runTest()
    test.run()
    createReport.getfp().close()

