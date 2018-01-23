# -*- coding: utf-8 -*-
from .basePage import basePage
from . import elementConfig as point


class BookingDetailPage(basePage):
    def verify_page(self):
        return super().isElement_exist(*point.BOOKING_DETAIL["header"])

    def get_flight_info(self, flight_trip):
        actual_result = {}
        for j in range(1, int(flight_trip)+1):
            flight_details = self.getElementlist(0, j, **point.SUMMARY["flight_detail_container"])
            for i in range(0, len(flight_details)):
                cabin = self.get_each_info(flight_details[i], *point.SUMMARY["cabin"])
                dst_terminal = self.get_each_info(flight_details[i], *point.SUMMARY["dst_terminal"])
                share = str(self.isElement_exist(flight_details[i], *point.SUMMARY["code_share"]))
                if "航站楼" in dst_terminal:
                    dst_terminal = dst_terminal.split(",")[1].strip(" ")
                else:
                    dst_terminal = ""
                stopover = self.get_each_info(flight_details[i], *point.SUMMARY["stopover"])
                actual_result["cabin_type" + str(j) + "_leg" + str(i+1)] = cabin
                actual_result["terminal_type" + str(j) + "_leg" + str(i+1)] = dst_terminal
                actual_result["stopover_type" + str(j) + "_leg" + str(i+1)] = stopover
                actual_result["share_type" + str(j) + "_leg" + str(i + 1)] = share
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

    def back_to_booking(self):
        self.back()