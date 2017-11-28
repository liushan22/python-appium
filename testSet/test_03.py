# -*- coding: utf-8 -*-
import unittest
from common.driver import driver
from common.log import logger
import common.report as report
import time
from selenium.webdriver.support.ui import WebDriverWait
from page.passengerListPage import passengerListPage
import page.elementConfig as point
finalclick = 0  # 最后点击的乘机人索引


class test_03(unittest.TestCase):
    """
    遍历booking中的乘机人列表，并提交
    """
    def setUp(self):
        self.log = logger(report.today_report_path).getlog()
        self.log.info("test_03")
        self.passengerListPage = passengerListPage()

    def test_passenger(self):
        time.sleep(5)
        global finalclick
        totalelement = 300  # 乘机人总数
        passengerListPage.find_elements(point.HOMEPAGE["find_flight"]).click()  # 进入找飞机页面
        passengerListPage.find_elements(point.FLIGHTPAGE["search"]).click()  # 搜索
        flight_results = passengerListPage.getElementlist(point.TIMELINE["flight_list"], point.TIMELINE["flight"])
        # 获得timeline航班列表
        flight_results[0].click()  # 点击第一条航班
        OTAs = passengerListPage.getElementlist(point.SUMMARY["OTA_list"], point.SUMMARY["OTA"])

        OTAs[0].click()
        # self.driver.find_element_by_id("com.igola.travel:id/add_passenger_layout").click()
        passengerListPage.find_elements(point.BOOKING["add_passenger"]).click()
        element = passengerListPage.getElementlist(point.BOOKING["passenger_list"], point.BOOKING["passenger"])
        finalclick = passengerListPage.clickElements(element, finalclick, point.BOOKING_PASSENGER["passenger"])
        while finalclick < totalelement:  # 如果最后点击的乘机人索引小于总共有的乘机人，则下滑
            passengerListPage.swipedown(1000)
            elements = passengerListPage.getElementlist(point.BOOKING["passenger_list"], point.BOOKING["passenger"])
            thisclick = (totalelement - finalclick) % 10  # 计算剩下未点击的乘机人数量 % 一页展示的数量
            if thisclick != 0:  # 剩下的未点击的乘机人数量不足一页时
                passengerListPage.clickElements(elements[-thisclick:], finalclick, point.BOOKING_PASSENGER["passenger"])
            else:
                passengerListPage.clickElements(element, finalclick, point.BOOKING_PASSENGER["passenger"])
        self.log.info("本次共检查%s条乘机人数据" % finalclick)

    def tearDown(self):
        passengerListPage.quit(super(passengerListPage))


