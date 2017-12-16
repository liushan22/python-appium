# -*- coding: utf-8 -*-
from basePage import basePage
import time
import elementConfig as point
from testSet.common.sreenshot import screenshot


class passengerListPage(basePage):

    def clickEachElements(self, elements, finalclick, *loc):
        """
        点击每个乘机人栏方法
        :param elements: 当前页面的乘机人列表
        :return: 最后点击的乘机人索引
        """
        for ele in elements:
            # ele.click()
            ele.click()
            self.find_element(*point.BOOKING_PASSENGER["submit_passenger"]).click()
            time.sleep(1)
            if not self.find_elements(*loc):
                time.sleep(2)
                self.back()
            finalclick += 1
        return finalclick

    @screenshot
    def select_passenger(self, *passenger_type):
        self.log.info("选择乘机人")
        isclick = False
        for passenger in passenger_type:
            while not isclick:
                elements = self.getElementlist(**point.BOOKING_PASSENGER["passenger_container"])
                for ele in elements:
                    self.log.debug(ele.text)
                    if ele.text == passenger:
                        ele.click()
                        isclick = True
                        break
                if not isclick:
                    self.swipedown(500)
        time.sleep(1)
        self.sumbit_passenger()

    def sumbit_passenger(self):
        self.log.info("提交乘机人")
        self.tap()

    @screenshot
    def getElementlist(self, **loc):
        """
        获取乘机人列表
        :return: 乘机人列表
        """
        dict = sorted(loc.items(), key=lambda d: d[0])
        loc1 = dict[1][1]
        loc2 = dict[2][1]
        # self.log.debug(loc1, loc2)
        element = self.find_element(*loc1)
        elements = element.find_elements(*loc2)
        assert len(elements) != 0, "页面异常"
        return elements




