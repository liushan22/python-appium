# -*- coding: utf-8 -*-

import unittest
from common.sreenshot import ScreenShot
from selenium.common.exceptions import WebDriverException
from common.log import logger
import common.report as report
from common.driver import driver


class test_02(unittest.TestCase):
    def setUp(self):
        self.dr = driver.__new__(driver)
        self.driver = self.dr.getDriver()
        self.log = logger(report.today_report_path).getlog()
        self.log.info("test_02")

    def test_passenger(self):
        self.log.info("test_passenger")
        self.driver.find_element_by_id("com.igola.travel:id/account_btn").click()
        islogin = self.driver.find_elements_by_id("com.igola.travel:id/name_tv")
        if not islogin:
            self.driver.find_element_by_id("com.igola.travel:id/traveller_ll").click()
            element = self.driver.find_element_by_id("com.igola.travel:id/passenger_recycler_view")
            elements = element.find_element_by_id("com.igola.travel:id/user_layout")
            for ele in elements:
                ele.click()
                self.driver.keyevent(4)  # 4代表返回具体查看http://www.cnblogs.com/zoro-robin/p/5640557.html
        else:
            self.log.info("未登录")

    def tearDown(self):
        pass
