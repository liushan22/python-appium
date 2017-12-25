# -*- coding: utf-8 -*-
from basePage import basePage
import elementConfig as point


class FlightPage(basePage):
    def select_ways(self, way):
        self.log.info(u"选择航程类型")
        way = int(way)
        elements = self.getElementlist(**point.FLIGHTPAGE["type_container"])
        elements[way].click()

    def go_citypage(self, city):
        self.log.info(u"选择%s地" % city)
        self.find_element(*point.FLIGHTPAGE[city]).click()

    def search(self):
        self.log.info(u"搜索")
        self.find_element(*point.FLIGHTPAGE["search"]).click()