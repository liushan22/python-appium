# -*- coding: utf-8 -*-
from basePage import basePage
import time


class passengerListPage(basePage):

    def clickEachElements(self, elements, finalclick, *loc):
        """
        点击每个乘机人栏方法
        :param elements: 当前页面的乘机人列表
        :return: 最后点击的乘机人索引
        """
        for ele in elements:
            ele.click()
            self.find_element(*loc).click()
            issubmit = self.find_elements(*loc)
            if not issubmit:
                time.sleep(2)
                self.back()
            time.sleep(3)
            finalclick += 1
        return finalclick



