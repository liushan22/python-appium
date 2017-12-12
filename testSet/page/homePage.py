# -*- coding: utf-8 -*-
from basePage import basePage
import elementConfig as point


class homePage(basePage):
    def go_flightPage(self):
        self.find_element(*point.HOMEPAGE["find_flight"]).click()  # 进入找飞机页面

