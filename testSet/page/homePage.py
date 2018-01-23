# -*- coding: utf-8 -*-
from .basePage import basePage
from . import elementConfig as point


class homePage(basePage):
    def go_flightPage(self):
        self.log.info("进入找飞机页面")
        self.find_element(*point.HOMEPAGE["find_flight"]).click()  # 进入找飞机页面

    def go_order(self):
        self.find_element(*point.HOMEPAGE["order"]).click()

