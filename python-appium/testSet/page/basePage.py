# -*- coding: utf-8 -*-
from testSet.common.driver import driver
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from testSet.common.log import logger
import testSet.common.report as report
from testSet.common.sreenshot import ScreenShot
from appium import webdriver
# testdriver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', driver.desired_caps)
port = ""
dev = ""


def setconfig(config, device):
    global port, dev
    port = config
    dev = device


class basePage(object):
    def __init__(self):
        #global testdriver
        #self.driver = testdriver
        # self.dr = driver()
        # self.dr.connect()
        # self.driver = self.dr.getDriver()
        global port, dev
        self.dr = driver(dev)
        self.dr.connect(port)
        self.driver = self.dr.getDriver()
        self.log = logger(report.today_report_path).getlog()


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

    def send_keys(self, value, clear_first=True, click_first=True, *loc):
        try:
            # loc = getattr(self, "_%s" % loc)  # getattr相当于实现self.loc
            value = str(int(value))
            if click_first:
                self.find_element(*loc).click()
            if clear_first:
                self.find_element(*loc).send_keys(value)
        except AttributeError:
            self.log.error("%s 页面中未能找到 %s 元素" % (self, loc))

    def back(self):
        self.driver.keyevent(4)  # 4代表返回具体查看http://www.cnblogs.com/zoro-robin/p/5640557.html

    # @ScreenShot(driver)
    def find_element(self, *loc):
        try:
            self.log.debug(*loc)
            element = WebDriverWait(self.driver, 10).until(lambda x: x.find_element(*loc))
            # element = self.driver.find_element(*loc)

            return element
        except:
            self.log.info("%s 页面没有找到%s元素" % (self, loc))

    # @ScreenShot(driver)
    def find_elements(self, *loc):
        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(*loc))
            return self.driver.find_elements(*loc)
        except:
            self.log.info("%s 页面没有找到%s元素" % (self, loc))

    # @ScreenShot(driver)
    def getElementlist(self, **loc):
        """
        获取乘机人列表
        :return: 乘机人列表
        """
        loc1 = loc.items()[0][1]
        loc2 = loc.items()[1][1]
        self.log.debug(loc1, loc2)
        element = self.find_element(*loc1)
        elements = element.find_elements(*loc2)
        return elements

    def quit(self):
        self.driver.quit()
