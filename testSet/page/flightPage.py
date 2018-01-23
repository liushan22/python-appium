# -*- coding: utf-8 -*-
from .basePage import basePage
from . import elementConfig as point
import time


class FlightPage(basePage):
    def select_ways(self, way):
        self.log.info("选择航程类型")
        way = int(way)
        elements = self.getElementlist(0, 1, **point.FLIGHTPAGE["type_container"])
        elements[way-1].click()

    def go_citypage(self, city):
        self.log.info("选择%s地" % city)
        self.find_element(*point.FLIGHTPAGE[city]).click()

    def search(self):
        self.log.info("搜索")
        self.find_element(*point.FLIGHTPAGE["search"]).click()

    def verify_page(self):
        return self.isElement_exist(*point.FLIGHTPAGE["search"])

    def select_cabin(self, cabin):
        self.log.info("选择舱位")
        self.find_element(*point.FLIGHTPAGE["cabin"]).click()
        num = self._cabin_to_number(cabin)
        for i in range(0, num):
            self.swipedown_little(0.95, 0.90)
            time.sleep(1)
        self.find_element(*point.FLIGHTPAGE["confirm"]).click()

    def _cabin_to_number(self,cabin):
        return {
            "经济舱": 0,
            "高端经济舱": 1,
            "商务舱": 2,
            "头等舱": 3
        }[cabin]