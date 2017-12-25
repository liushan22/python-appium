# -*- coding: utf-8 -*-
from basePage import basePage
import time
import elementConfig as point
from testSet.common.sreenshot import screenshot
from testSet.common.sreenshot import testcase_exception


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

    @testcase_exception
    def go_passengerpage(self, passenger):
        self.log.info("进入乘机人编辑页")
        isclick = False
        while not isclick:
            elements = self.getElementlist(0, 2, **point.BOOKING_PASSENGER["passenger_container"])
            for ele in elements:
                name = ele.find_elements(*point.BOOKING_PASSENGER["passenger_container"]["passenger_name"])
                if name[0].text == passenger:
                    edit = ele.find_elements(*point.BOOKING_PASSENGER["passenger_container"]["passenger_edit"])
                    if len(edit) != 0:
                        self.log.info(name[0].text)
                        edit[0].click()
                        isclick = True
                        break
                elif name[0].text == "HOME ISSUEATMOEA":
                    self.log.info("没有找到该乘机人")
                    return
            if not isclick:
                self.swipedown(500)

    def select_passenger(self, *passenger_type):
        self.log.info("选择乘机人")
        isclick = False
        for passenger in passenger_type:
            while not isclick:
                elements = self.getElementlist(3, 2, **point.BOOKING_PASSENGER["passenger_container"])
                for ele in elements:
                    if ele.text == passenger:
                        self.log.info(ele.text)
                        ele.click()
                        isclick = True
                        break
                if not isclick:
                    self.swipedown(500)
        time.sleep(1)
        self.sumbit_passenger()

    def sumbit_passenger(self):
        self.log.info("提交乘机人")
        self.tap("123")

    @screenshot
    def find_title(self):
        assert not self.isElement_exist(*point.PASSENGER["title"])

    @screenshot
    def getElementlist(self, x, y, **loc):
        """
        获取乘机人列表
        :return: 乘机人列表
        """
        dict = sorted(loc.items(), key=lambda d: d[0])
        loc1 = dict[y][1]
        loc2 = dict[x][1]
        # self.log.debug(loc1, loc2)
        element = self.find_element(*loc1)
        elements = element.find_elements(*loc2)
        assert len(elements) != 0, "乘机人列表页为空"
        return elements





