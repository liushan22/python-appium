# coding=utf-8
from appium import webdriver
import time
import unittest
import common.driver as driver
from common.sreenshot import ScreenShot
from selenium.common.exceptions import WebDriverException
from common.log import logger
import common.report as report
dr = driver.driver

class test_01(unittest.TestCase):

    def setUp(self):
        global dr
        self.driver = dr
        self.log = logger(report.today_report_path).getlog()
        self.log.info("test_01")

    def get_size(self):
        x = self.driver.get_window_size()['width']
        y = self.driver.get_window_size()['height']
        return (x, y)

    def swipeleft(self, t):
        l = self.get_size()
        x1 = int(l[0]*0.75)
        y1 = int(l[1]*0.5)
        x2 = int(l[0]*0.05)
        self.driver.swipe(x1, y1, x2, y1, t)

    def test_login(self):
        self.log.info("login")
        try:
            time.sleep(15)
            # self.swipeleft(1000)
            # time.sleep(1)
            # self.swipeleft(1000)
            # time.sleep(1)
            # self.swipeleft(1000)
            # time.sleep(1)
            # self.swipeleft(1000)
            #
            # time.sleep(3)
            # self.driver.find_element_by_id("com.igola.travel:id/go_2_main_btn").click()
            self.driver.find_element_by_id("com.igola.travel:id/account_btn").click()
            time.sleep(1)
            self.driver.find_element_by_id("com.igola.travel:id/login_btn").click()
            self.driver.find_element_by_id("com.igola.travel:id/account_et").send_keys('18819490408')
            self.driver.find_element_by_id("com.igola.travel:id/password_et").send_keys('321321321')
            self.driver.find_element_by_id("com.igola.travel:id/login_btn").click()
            # self.assertIsNotNone(self.driver.find_elements_by_id(""), "登录失败")
            #name = self.driver.find_element_by_id("com.igola.travel:id/name_tv").text
        except WebDriverException as e:
            raise
        finally:
            ScreenShot(self.driver).get_screenshot()

    def tearDown(self):
        print "test over"


