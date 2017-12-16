# -*- coding: utf-8 -*-
from testSet.common.driver import driver
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from testSet.common.log import logger
import testSet.common.report as report
import os
from testSet.common.sreenshot import screenshot
from testSet.public.tran_type import TranType
from selenium.common.exceptions import NoSuchElementException
from appium import webdriver
# testdriver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', driver.desired_caps)
parent_path=os.path.abspath(os.path.dirname(os.path.realpath(__file__))+os.path.sep+"..")
report_path = os.path.join(os.path.dirname(parent_path), 'result')
today = time.strftime("%Y%m%d", time.localtime(time.time()))
today_report_path = report_path + "\\" + today
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
        #global testdriver
        #self.driver = testdriver
        # self.dr = driver()
        # self.dr.connect()
        # self.driver = self.dr.getDriver()
        global port, dev, isinit
        if not isinit:
            self.dr = driver(dev)
            self.dr.connect(port)
            isinit = True
            self.driver = self.dr.getDriver()
        else:
            self.driver = driver(dev).getDriver()
        l = logger(report.today_report_path)
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
        y1 = int(l[1]*0.75)
        y2 = int(l[1]*0.05)
        self.driver.swipe(x1, y1, x1, y2, t)

    @screenshot
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

    @screenshot
    def find_element(self, *loc):
        element = WebDriverWait(self.driver, 10).until(lambda x: x.find_element(*loc))
        return element

    @screenshot
    def find_elements(self, *loc):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(*loc))
        return self.driver.find_elements(*loc)

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

    def hide_keyboard(self):
        self.driver.hide_keyboard()

    def tap(self):
        self.driver.tap([(584, 68), (704, 128)], 500)

    def isElement_exist(self, *loc):
        try:
            WebDriverWait(self.driver, 10).until(lambda x: x.find_element(*loc))
            return True
        except:
            return False

    def quit(self):
        global isinit
        isinit = False
        self.driver.quit()
