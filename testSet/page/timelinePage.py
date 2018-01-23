# -*- coding: utf-8 -*-
from .basePage import basePage
from . import elementConfig as point
i = 1


class TimelinePage(basePage):
    def select_flight(self, price):
        self.log.info("选择 timeline 航班")
        flight_results = self.getElementlist(6, 3, **point.TIMELINE["flight_container"])
        # 获得timeline航班列表
        for result in flight_results:
            if result.text == price:
                result.click()  # 点击第一条航班
                break

    def get_flight_info(self):
        global i
        flight_results = self.getElementlist(2, 3, **point.TIMELINE["flight_container"])
        code_share = self.isElement_exist(flight_results[0], *point.TIMELINE["flight_container"]["code_share"])
        # stop = self.get_each_info(flight_results[0], *point.TIMELINE["flight_container"]["stop"])
        # change = self.get_each_info(flight_results[0], *point.TIMELINE["flight_container"]["change"])
        # stopover = self.isElement_exist(flight_results[0], *point.TIMELINE["flight_container"]["stopover"])
        stopover = ""
        stop = ""
        change = ""
        actual_result = {"share_type" + str(i): code_share,
                         "stop_type" + str(i): stop,
                         "change_type" + str(i): change,
                         "stopover_type" + str(i): stopover
                         }
        i = i + 1
        return actual_result

    def get_each_info(self, flight_results, *loc):
        not_exist = ""
        if self.isElement_exist(flight_results, *loc):
            return flight_results.find_element(*loc).text
        else:
            return not_exist

    def isElement_exist(self, flight_results, *loc):
        try:
            flight_results.find_element(*loc)
            return True
        except:
            return ""

    def verify_page(self):
        return super().isElement_exist(*point.TIMELINE["header"])


