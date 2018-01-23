# -*- coding: utf-8 -*-
from .basePage import basePage
from . import elementConfig as point


class OrderDetailPage(basePage):
    def go_passengerDetail(self):
        self.log.info("进入订单乘机人详情页")
        self.find_element(*point.ORDER_PASSENGER["passenger"]).click()

    def collapse(self):
        if super().isElement_exist(*point.SUMMARY["collapse"]):
            self.find_element(*point.SUMMARY["collapse"]).click()

    def check_passenger_info(self, name, type, id, gender, nationality):
        self.log.info("检查乘机人信息")
        assert self.find_element(*point.ORDER_PASSENGER["type"]).text == type
        assert self.find_element(*point.ORDER_PASSENGER["id_number"]).text == id
        first_name = name.split(' ')[0]
        last_name = name.split(' ')[1]
        assert self.find_element(*point.ORDER_PASSENGER["first_name"]).text == first_name
        assert self.find_element(*point.ORDER_PASSENGER["last_name"]).text == last_name
        assert self.find_element(*point.ORDER_PASSENGER["gender"]).text == gender
        assert self.find_element(*point.ORDER_PASSENGER["nationality"]).text == nationality

    def verify_page(self):
        return super().isElement_exist(*point.ORDER["price"])

    def get_flight_info(self, flight_trip):
        actual_result = {}
        for j in range(1, int(flight_trip)+1):
            flight_details = self.getElementlist(0, j, **point.SUMMARY["flight_detail_container"])
            for i in range(0, len(flight_details)):
                cabin = self.get_each_info(flight_details[i], *point.SUMMARY["cabin"])
                dst_terminal = self.get_each_info(flight_details[i], *point.SUMMARY["dst_terminal"])
                if "航站楼" in dst_terminal:
                    dst_terminal = dst_terminal.split(",")[1].strip(" ")
                else:
                    dst_terminal = ""
                actual_result["cabin_type" + str(j) + "_leg" + str(i+1)] = cabin
                actual_result["terminal_type" + str(j) + "_leg" + str(i+1)] = dst_terminal
            if len(flight_details) > 1:
                transfers = self.getElementlist(3, j, **point.SUMMARY["flight_detail_container"])
                for z in range(0, len(transfers)):
                    trans = transfers[z].text
                    trans = trans[4:]
                    actual_result["transfer_type" + str(j) + "_leg" + str(z + 2)] = trans
                self.swipedown(500)
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
