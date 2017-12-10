# -*- coding: utf-8 -*-
from basePage import basePage
import time
import elementConfig as point


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



