# -*- coding: utf-8 -*-
from testSet.common.driver import driver
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from testSet.common.log import logger
import testSet.common.report as report
import os
from testSet.util.tran_type import TranType
from . import elementConfig as point
import testSet.util.date as date
from selenium.common.exceptions import NoSuchElementException
from appium import webdriver
port = ""
dev = ""
c = 0
isinit = False


def setconfig(config, device):
    global port, dev
    port = config
    dev = device


class basePage(object):
    def __init__(self):
        global port, dev, isinit
        if not isinit:
            self.dr = driver(dev)
            self.dr.connect(port)
            isinit = True
            self.driver = self.dr.getDriver()
        else:
            self.driver = driver(dev).getDriver()
        l = logger(date.today_report_path)
        self.log = l.getlog()
        self.tran_type = TranType()

    def get_size(self):
        """
        获取手机屏幕的大小
        :return: 手机屏幕的宽高
        """
        x = self.driver.get_window_size()['width']
        y = self.driver.get_window_size()['height']
        return x, y

    def swipedown(self, t):
        """
        下滑方法
        :param t:滑动需要的时间，以毫秒为单位
        :return: null
        """
        l = self.get_size()
        x1 = int(l[0]*0.5)
        y1 = int(l[1]*0.60)
        y2 = int(l[1]*0.05)
        self.driver.swipe(x1, y1, x1, y2, t)

    def swipedown_little(self, before, after):
        """
        下滑方法
        :param t:滑动需要的时间，以毫秒为单位
        :return: null
        """
        l = self.get_size()
        x1 = int(l[0]*0.5)
        y1 = int(l[1]*before)
        y2 = int(l[1]*after)
        self.driver.swipe(x1, y1, x1, y2, 500)

    def send_keys(self, value, clear_first=True, click_first=True, *loc):
        # loc = getattr(self, "_%s" % loc)  # getattr相当于实现self.loc
        value = self.tran_type.tran_type(value)
        if click_first:
            self.find_element(*loc).click()
            self.hide_keyboard()
        if clear_first:
            self.find_element(*loc).send_keys(value)

    def back(self):
        self.driver.keyevent(4)  # 4代表返回具体查看http://www.cnblogs.com/zoro-robin/p/5640557.html

    def find_element(self, *loc):
        element = WebDriverWait(self.driver, 10).until(lambda x: x.find_element(*loc))
        return element

    def find_elements(self, *loc):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(*loc))
        elements = self.driver.find_elements(*loc)
        assert len(elements) != 0
        return elements

    def getElementlist(self, x, y, **loc):
        """
        获取乘机人列表
        :return: 乘机人列表
        """
        dict = sorted(list(loc.items()), key=lambda d: d[0])
        loc1 = dict[y][1]
        loc2 = dict[x][1]
        # self.log.debug(loc1, loc2)
        element = self.find_element(*loc1)
        elements = element.find_elements(*loc2)
        return elements

    def hide_keyboard(self):
        self.driver.hide_keyboard()

    def tap(self, loc):
        if self.isElement_exist(*point.BOOKING_PASSENGER["submit_passenger"]):
            self.driver.tap([(584, 68), (704, 128)], 500)

    def isElement_exist(self, *loc):
        try:
            WebDriverWait(self.driver, 3).until(lambda x: x.find_element(*loc))
            return True
        except:
            return False

    def isElement_clickable(self, *loc):
        element = self.find_element(*loc)
        return element.clickable

    def quit(self):
        global isinit
        isinit = False
        self.driver.quit()
