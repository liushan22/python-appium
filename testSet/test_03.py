# -*- coding: utf-8 -*-
import unittest
from common.driver import driver
from common.log import logger
import common.report as report
import time
from selenium.webdriver.support.ui import WebDriverWait
finalclick = 0  # 最后点击的乘机人索引


class test_03(unittest.TestCase):
    """
    遍历booking中的乘机人列表，并提交
    """
    def setUp(self):
        self.driver = driver().getDriver()
        self.log = logger(report.today_report_path).getlog()
        self.log.info("test_02")

    def get_size(self):
        """
        获取手机屏幕的大小
        :return: 手机屏幕的宽高
        """
        x = self.driver.get_window_size()['width']
        y = self.driver.get_window_size()['height']
        return (x,y)

    def swipedown(self, t):
        """
        下滑方法
        :param t:滑动需要的时间，以毫秒为单位
        :return: null
        """
        l = self.get_size()
        x1 = int(l[0]*0.5)
        y1 = int(l[1]*0.85)
        y2 = int(l[1]*0.05)
        self.driver.swipe(x1, y1, x1, y2, t)

    def clickElements(self, elements):
        """
        点击每个乘机人栏方法
        :param elements: 当前页面的乘机人列表
        :return: 最后点击的乘机人索引
        """
        global finalclick
        for ele in elements:
            try:
                ele.click()
                WebDriverWait(self.driver, 10).until(lambda x: x.find_element_by_id("com.igola.travel:id/submit_cv")).click()
                # self.driver.find_element_by_id("com.igola.travel:id/submit_cv").click()
                time.sleep(2)
                issubmit = self.driver.find_elements_by_id("com.igola.travel:id/passenger_recycler_view")
                if not issubmit:
                    time.sleep(2)
                    self.driver.keyevent(4)  # 4代表返回具体查看http://www.cnblogs.com/zoro-robin/p/5640557.html
                time.sleep(3)
                finalclick += 1
            except 
        return finalclick

    def getElementList(self):
        """
        获取乘机人列表
        :return: 乘机人列表
        """
        element = self.driver.find_element_by_id("com.igola.travel:id/passenger_recycler_view")
        elements = element.find_elements_by_id("com.igola.travel:id/user_layout")
        return elements

    def test_passenger(self):
        global finalclick
        totalelement = 300
        # self.driver.find_element_by_id("com.igola.travel:id/find_flight_btn").click()
        WebDriverWait(self.driver, 10).until(lambda x: x.find_element_by_id("com.igola.travel:id/find_flight_btn")).click()
        WebDriverWait(self.driver, 3).until(
            lambda x: x.find_element_by_id("com.igola.travel:id/search_btn")).click()
        #self.driver.find_element_by_id("com.igola.travel:id/search_btn").click()
        flight_result = WebDriverWait(self.driver, 5).until(
            lambda x: x.find_element_by_id("com.igola.travel:id/results_recycler_view")).click()
        # flight_result = self.driver.find_element_by_id("com.igola.travel:id/results_recycler_view")
        if flight_result:
            flight_results = flight_result.find_elements_by_class_name("android.widget.RelativeLayout")
            flight_results[0].click()
            # OTA_list = self.driver.find_element_by_id("com.igola.travel:id/book_list")
            OTA_list = WebDriverWait(self.driver, 5).until(
                lambda x: x.find_element_by_id("com.igola.travel:id/book_list")).click()
            OTAs = OTA_list.find_elements_by_class_name("android.widget.RelativeLayout")
            OTAs[0].click()
            # self.driver.find_element_by_id("com.igola.travel:id/add_passenger_layout").click()
            WebDriverWait(self.driver, 5).until(
                lambda x: x.find_element_by_id("com.igola.travel:id/add_passenger_layout")).click()
            element = self.getElementList()
            finalclick = self.clickElements(element)
            while finalclick < totalelement:  # 如果最后点击的乘机人索引小于总共有的乘机人，则下滑
                self.swipedown(1000)
                elements = self.getElementList()
                thisclick = (totalelement - finalclick) % 10  # 计算剩下未点击的乘机人数量 % 一页展示的数量
                if thisclick != 0:  # 剩下的未点击的乘机人数量不足一页时
                    self.clickElements(elements[-thisclick:])
                else:
                    self.clickElements(elements)
            self.log.info("本次共检查%s条乘机人数据" % finalclick)

    def tearDown(self):
        self.driver.quit()


