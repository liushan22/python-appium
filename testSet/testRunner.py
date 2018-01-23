# -*- coding: utf-8 -*-
import threading
import unittest
from testSet.testcase.test_flight import Test_flight as testcase1
from testSet.testcase.test_test import test as testcase
import testSet.common.report as report
import testSet.page.basePage as basePage
from testSet.common.myServer import myServer
import time
from testSet.common.log import logger
import testSet.util.date as date

createReport = report.report()


class runTest():
    def __init__(self):
        pass

    def run(self, config, device):
        time.sleep(8)
        basePage.setconfig(config, device)
        # suite = unittest.TestSuite()
        # suite.addTest(testcase1("test_go_flightpage"))
        # suite.addTest(testcase1("test_search"))
        suite = unittest.TestLoader().loadTestsFromTestCase(testcase1)
        runner = createReport.getReportConfig()
        runner.run(suite)
        ms.quit()

    def getDriver(self, driver):
        return driver


class myThread(threading.Thread):
    def __init__(self, device, config):
        threading.Thread.__init__(self)
        self.device = device
        self.config = config

    def run(self):
        if __name__ == '__main__':
            test = runTest()
            test.run(self.config, self.device)
            # test.driverquit()
            createReport.getfp().close()
            log = logger(date.today_report_path).getlog()
            log.info(self.device + "test over")

if __name__ == '__main__':
    try:
        devices = ["192.168.20.254:5555"]
        theading_pool = []
        for device in devices:
            ms = myServer(device)
            config = ms.run()
            t = myThread(device, config)
            theading_pool.append(t)
        for t in theading_pool:
            t.start()
            time.sleep(5)
        for t in theading_pool:

            t.join()
    except:
        print("线程运行失败")
        raise

