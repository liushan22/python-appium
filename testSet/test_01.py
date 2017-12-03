# coding=utf-8
from appium import webdriver
import time
import unittest
from common.driver import driver
from common.sreenshot import ScreenShot
from selenium.common.exceptions import WebDriverException
from common.log import logger
import common.report as report
from page.loginPage import loginPage
import page.elementConfig as point
import xlrd  #excel驱动程序
from xlrd import open_workbook


class test_01(unittest.TestCase):

    def setUp(self):
        # global port, device
        # self.driver = driver(device).connect(port)
        # self.driver = self.driver.getDriver()
        self.log = logger(report.today_report_path).getlog()
        self.log.info("test_01")
        self.loginPage = loginPage()

    def getlogin(self, arg1, arg2, arg3, arg4):
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
            accout = arg1
            password = arg2
            expected_result = arg3
            self.loginPage.find_element(*point.HOMEPAGE["MY"]).click()
            time.sleep(1)
            self.loginPage.find_element(*point.MY["login"]).click()
            self.loginPage.send_keys(accout, True, True, *point.LOGIN["account"])
            self.loginPage.send_keys(password, True, True, *point.LOGIN["password"])
            self.loginPage.find_element(*point.LOGIN["submit"]).click()
            actual_result = self.loginPage.find_element(*point.LOGIN["error_msg"])
            self.assertEqual(expected_result, actual_result.text)
            # self.assertIsNotNone(self.driver.find_elements_by_id(""), "登录失败")
            #name = self.driver.find_element_by_id("com.igola.travel:id/name_tv").text
        except WebDriverException as e:
            raise

    @staticmethod
    def getTestFunc(arg1, arg2, arg3, arg4):
        def func(self):
            self.getlogin(arg1, arg2, arg3, arg4)

        return func

    def tearDown(self):
        self.loginPage.quit()
        print "test over"





