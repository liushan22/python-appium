# -*- coding: utf-8 -*-
from driver import driver
import time
from selenium.webdriver.support.ui import WebDriverWait


class element:
    def __init__(self):
        self.driver = driver().getDriver()

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
            ele.click()
            time.sleep(1)
            self.driver.find_element_by_id("com.igola.travel:id/submit_cv").click()
            time.sleep(4)
            issubmit = self.driver.find_elements_by_id("com.igola.travel:id/passenger_recycler_view")
            if not issubmit:
                time.sleep(2)
                self.driver.keyevent(4)  # 4代表返回具体查看http://www.cnblogs.com/zoro-robin/p/5640557.html
            time.sleep(3)
            finalclick += 1
        return finalclick

    def getElementList(self, listname, ele):
        """
        获取乘机人列表
        :return: 乘机人列表
        """
        element = self.driver.find_element_by_id("com.igola.travel:id/passenger_recycler_view")
        elements = element.find_elements_by_id("com.igola.travel:id/user_layout")
        return elements

    def click(self, ele):
        pass

    def send_keys(self, ele):
        pass

    def keyevent(self, ele, key):
        pass

    def wait(self):
        WebDriverWait(self.driver, 10).until(lambda x: x.find_element_by_id("com.igola.travel:id/submit_cv"))