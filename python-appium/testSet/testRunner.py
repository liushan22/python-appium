# -*- coding: utf-8 -*-


import unittest

import common.report as report
from common.myServer import myServer
from test_01 import test_01 as testcase1
from test_02 import test_02 as testcase2
from test_03 import test_03 as testcase3
import threading
import xlrd  #excel驱动程序
from xlrd import open_workbook
import page.basePage as basePage

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

    def run(self,config, device, *casename):
        # ms = myServer(device)
        # config = ms.run()
        time.sleep(8)
        # driver = ms.isServerStart()
        # if driver:
        basePage.setconfig(config, device)
        suite = unittest.TestSuite()
        for case in casename:
            suite.addTest(testcase1(case))
        # suite.addTest(testcase2("test_passenger"))
        # suite.addTest(testcase3("test_passenger"))
        runner = createReport.getReportConfig()
        runner.run(suite)
        ms.quit()
       # else:
           #  print "appium is not start"

    def getDriver(self, driver):
        return driver


class myThread(threading.Thread):
    def __init__(self, device, config):
        threading.Thread.__init__(self)
        self.device = device
        self.config = config

    def __generateTestCases(self):
        # parent_path = os.path.abspath(os.path.dirname(os.path.realpath(__file__)))
        caselist_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'caselist')
        data = open_workbook(caselist_path + "\\" + 'login.xlsx')  # 打开文件
        table = data.sheet_by_index(0)  # 遍历所有数据
        # datas = table.row_values(0) # 获取整列数据
        nrows = table.nrows  # 获得行数
        list = []
        for i in range(1, nrows):  # 忽略表头 ，开始遍历
            datas = table.row_values(i)  # 获得每行的数据
            list.append(datas)  # 加载到list中

        print(list)
        casename = []
        for args in list:
            print(args)
            setattr(testcase1, 'test_func_%s' % args[3],
                    testcase1.getTestFunc(*args))  # 通过setattr自动为TestCase类添加成员方法，方法以“test_func_”开头
            casename.append('test_func_%s' % args[3])
        return casename

    def run(self):
        if __name__ == '__main__':
            casename = self.__generateTestCases()
            test = runTest()
            test.run(self.config, self.device, *casename)
            # test.driverquit()
            createReport.getfp().close()
            log = logger(report.today_report_path).getlog()
            log.info("test over")

if __name__ == '__main__':
    try:
        devices = ["8885dc17", "33fd33df"]
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
        print "线程运行失败"
