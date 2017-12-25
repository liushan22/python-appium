# -*- coding: utf-8 -*-
from basePage import basePage
import elementConfig as point
from testApp.testSet.common.sreenshot import screenshot


class BookingPage(basePage):
    def go_passengerPage(self):
        self.log.info("进入乘机人页面")
        self.find_element(*point.BOOKING["add_passenger"]).click()

    def go_contactPage(self):
        self.log.info("进入联系人页面")
        self.find_element(*point.BOOKING["add_contact"]).click()

    def submit_order(self):
        self.log.info("提交订单")
        self.find_element(*point.BOOKING["submit_order"]).click()

    def go_insurance(self):
        self.log.info("进入保险页面")
        self.find_element(*point.BOOKING["add_insurance"]).click()

    def go_couponPage(self):
        self.log.info("进入优惠券页面")
        self.find_element(*point.BOOKING["add_coupon"]).click()

    @screenshot
    def find_title(self):
        if not self.isElement_exist(*point.BOOKING["add_passenger"]):
            if self.isElement_exist(*point.BOOKING["search_other_fight"]):
                self.log.info("验价失败，出现打包验价弹框")
                self.find_element(*point.BOOKING["search_other_fight"]).click()
            elif self.isElement_exist(*point.BOOKING["error"]):
                self.log.info("验价失败")
                self.find_element(*point.BOOKING["error"]).click()
                self.find_element(*point.SUMMARY["retry"]).click()
            return False
        else:
            return True

    def check_sumitbtn_clickable(self):
        self.log.info("检查提交按钮是否可点击")
        self.isElement_clickable(*point.BOOKING["submit_order"])


