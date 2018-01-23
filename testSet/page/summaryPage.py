# -*- coding: utf-8 -*-
from .basePage import basePage
from . import elementConfig as point
import time


class SummaryPage(basePage):
    def select_ota(self):
        time.sleep(1)
        self.log.info("选择 ota")
        OTAs = self.getElementlist(0, 2, **point.SUMMARY["OTA_container"])
        time.sleep(1)
        OTAs[0].click()

    def verify_page(self):
        return super().isElement_exist(*point.SUMMARY["OTA_container"]["OTA_list"])

    def collapse(self):
        if super().isElement_exist(*point.SUMMARY["collapse"]):
            self.find_element(*point.SUMMARY["collapse"]).click()

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
                    actual_result["transfer_type" + str(j) + "_leg" + str(z+2)] = trans
                self.swipedown(500)
        return actual_result

    def get_each_info(self, flight_results, *loc):
        not_exist = ""
        if self.isElement_exist(flight_results, *loc):
            return flight_results.find_element(*loc).text
        else:
            return not_exist

    def check_cabin(self, flight_trip, *trip):
        type = 1
        leg = 1
        element = self.find_element(*point.SUMMARY["OTA_container"]["OTA_cabin"])
        if len(element.text) > 7:
            time.sleep(2)
            element.click()
            cabin_list = self.getElementlist(0, 1, **point.SUMMARY["multi_cabin_container"])
            cabins_result = {}
            for i in range(0, len(cabin_list)):
                if i % 2 == 1:
                    cabins_result["cabin_type" + str(type) + "_leg" + str(leg)] = cabin_list[i].text
                    leg = leg + 1
                elif cabin_list[i].text in trip and type < int(flight_trip):
                    type = type + 1
                    leg = 1
            self.find_element(*point.SUMMARY["close"]).click()
            return element.text.strip(", "), cabins_result
        else:
            return element.text.strip(", ")

    def isElement_exist(self, flight_results, *loc):
        try:
            flight_results.find_element(*loc)
            return True
        except:
            return ""
