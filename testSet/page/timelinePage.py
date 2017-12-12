# -*- coding: utf-8 -*-
from basePage import basePage
import elementConfig as point


class TimelinePage(basePage):
    def select_flight(self):
        flight_results = self.getElementlist(**point.TIMELINE["flight_container"])
        # 获得timeline航班列表
        flight_results[0].click()  # 点击第一条航班