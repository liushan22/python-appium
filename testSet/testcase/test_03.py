# -*- coding: utf-8 -*-
import unittest
from testSet.common.driver import driver
from testSet.common.log import logger
import testSet.common.report as report
import time
from testSet.page.passengerListPage import passengerListPage
import testSet.page.elementConfig as point
from selenium.common.exceptions import WebDriverException
from testSet.common.sreenshot import screenshot
from testSet.common.driver import driver
finalclick = 0  # 最后点击的乘机人索引

__metaclass__ = type


class test_03(unittest.TestCase):
    """
    遍历booking中的乘机人列表，并提交
    """
    def setUp(self):
        self.log = logger(report.today_report_path).getlog()
        self.log.info("test_03")
        self.passengerListPage = passengerListPage()

    @screenshot
    def test_passenger(self):
        time.sleep(5)
        global finalclick
        totalelement = 2  # 乘机人总数
        self.passengerListPage.find_element(*point.HOMEPAGE["find_flight"]).click()  # 进入找飞机页面
        self.passengerListPage.find_element(*point.FLIGHTPAGE["search"]).click()  # 搜索
        flight_results = self.passengerListPage.getElementlist(**point.TIMELINE["flight_container"])
        # 获得timeline航班列表
        flight_results[0].click()  # 点击第一条航班
        OTAs = self.passengerListPage.getElementlist(**point.SUMMARY["OTA_container"])
        OTAs[0].click()
        # self.driver.find_element_by_id("com.igola.travel:id/add_passenger_layout").click()
        self.passengerListPage.find_element(*point.BOOKING["add_passenger"]).click()

        element = self.passengerListPage.getElementlist(**point.BOOKING_PASSENGER["passenger_container"])
        self.assertNotEqual(len(element), 0, "no passenger")
        finalclick = self.passengerListPage.clickEachElements(element, finalclick, *point.BOOKING_PASSENGER["passenger_container"]["edit"])
        while finalclick < totalelement:  # 如果最后点击的乘机人索引小于总共有的乘机人，则下滑
            self.passengerListPage.swipedown(1000)
            elements = self.passengerListPage.getElementlist(**point.BOOKING_PASSENGER["passenger_container"])
            thisclick = (totalelement - finalclick) % 10  # 计算剩下未点击的乘机人数量 % 一页展示的数量
            if thisclick != 0:  # 剩下的未点击的乘机人数量不足一页时
                self.passengerListPage.clickEachElements(elements[-thisclick:], finalclick, *point.BOOKING_PASSENGER["passenger_container"]["edit"])
            else:
                self.passengerListPage.clickEachElements(element, finalclick, *point.BOOKING_PASSENGER["passenger_container"]["edit"])
        self.log.info("本次共检查%s条乘机人数据" % finalclick)

    def tearDown(self):
        self.passengerListPage.quit()



