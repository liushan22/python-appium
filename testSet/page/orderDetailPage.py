# -*- coding: utf-8 -*-
from basePage import basePage
import elementConfig as point
from testApp.testSet.common.sreenshot import testcase_exception


class OrderDetailPage(basePage):
    def go_passengerDetail(self):
        self.log.info("进入订单乘机人详情页")
        self.find_element(*point.ORDER_PASSENGER["passenger"]).click()

    def check_info(self, name, type, id, gender, nationality):
        self.log.info("检查乘机人信息")
        assert self.find_element(*point.ORDER_PASSENGER["type"]).text == type
        assert self.find_element(*point.ORDER_PASSENGER["id_number"]).text == id
        first_name = name.split(' ')[0]
        last_name = name.split(' ')[1]
        assert self.find_element(*point.ORDER_PASSENGER["first_name"]).text == first_name
        assert self.find_element(*point.ORDER_PASSENGER["last_name"]).text == last_name
        assert self.find_element(*point.ORDER_PASSENGER["gender"]).text == gender
        assert self.find_element(*point.ORDER_PASSENGER["nationality"]).text == nationality
