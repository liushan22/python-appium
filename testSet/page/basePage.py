# -*- coding: utf-8 -*-
from testApp.testSet.common.driver import driver
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from testApp.testSet.common.log import logger
import testApp.testSet.common.report as report
import os
from testApp.testSet.common.sreenshot import screenshot
from appium import webdriver
# testdriver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', driver.desired_caps)
parent_path=os.path.abspath(os.path.dirname(os.path.realpath(__file__))+os.path.sep+"..")
report_path = os.path.join(os.path.dirname(parent_path), 'result')
today = time.strftime("%Y%m%d", time.localtime(time.time()))
today_report_path = report_path + "\\" + today
port = ""
dev = ""
c = 0


def setconfig(config, device):
    global port, dev
    port = config
    dev = device


# def sreenshot(func):
#     def inner(self, *args, **kwargs):
#         global c
#         try:
#             f = func(self, *args, **kwargs)
#             return f
#         except Exception:
#             self.log.info("screenshot")
#             self.log.info(report.today_report_path)
#             pngname = func.__name__ + str(c) + ".png"
#             self.driver.get_screenshot_as_file(today_report_path + "\\" + pngname)
#             print today_report_path + "\\" + pngname
#             c += 1 # 失败后截图
#     return inner


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
        # self.driver = basePage.testdriver
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

    @screenshot
    def find_element(self, *loc):
        try:
            # self.log.debug(*loc)
            element = WebDriverWait(self.driver, 10).until(lambda x: x.find_element(*loc))
            # element = self.driver.find_element(*loc)

            return element
        except:
            self.log.info("%s 页面没有找到%s元素" % (self, loc))

    @screenshot
    def find_elements(self, *loc):
        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(*loc))
            return self.driver.find_elements(*loc)
        except:
            self.log.info("%s 页面没有找到%s元素" % (self, loc))

    @screenshot
    def getElementlist(self, **loc):
        """
        获取乘机人列表
        :return: 乘机人列表
        """
        dict = sorted(loc.items(), key=lambda d: d[0])
        loc1 = dict[1][1]
        loc2 = dict[0][1]
        # self.log.debug(loc1, loc2)
        element = self.find_element(*loc1)
        elements = element.find_elements(*loc2)
        return elements

    def quit(self):
        self.driver.quit()
