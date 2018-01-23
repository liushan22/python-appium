# -*- coding: utf-8 -*-
from .basePage import basePage
from . import elementConfig as point
import time
from testSet.common.sreenshot import screenshot


class PaymentPage(basePage):
    @screenshot
    def select_each_payment(self):
        self.log.info("选择支付方式并点击支付")
        assert self.isElement_exist(*point.PAYMENT["pay"]), "支付页面报错"
        elements = self.getElementlist(**point.PAYMENT["payment_container"])
        for ele in elements:
            ele.click()
            self.find_element(*point.PAYMENT["pay"]).click()
            time.sleep(5)
            assert not self.isElement_exist(*point.PAYMENT["pay"]), "支付跳转错误"
            while not self.isElement_exist(*point.PAYMENT["pay"]):
                self.back()

    def select_payment(self):
        self.log.info("选择支付方式并点击支付")
        assert self.isElement_exist(*point.PAYMENT["pay"]), "支付页面报错"
        elements = self.getElementlist(**point.PAYMENT["payment_container"])
        elements[0].click()
        self.find_element(*point.PAYMENT["pay"]).click()
        self.pay()

    def pay(self):
        pay_loc = [(30, 1166), (690, 1250)]
        self.tap(pay_loc)
        pwd_loc = [[(240, 1066), (479, 1172)], [(0, 852), (239, 958)], [(240, 852), (479, 958)],
                   [(240, 852), (479, 958)], [(240, 959), (479, 1065)], [(240, 1066), (479, 1172)]]
        for i in pwd_loc:
            self.tap(i)
            time.sleep(1)

    def tap(self, loc):
        self.driver.tap(loc, 500)

    def verify_page(self):
        return self.isElement_exist(*point.PAYMENT["pay"])

    def check_cabin(self):
        cabin = self.find_element(*point.PAYMENT["cabin"]).text
        return cabin

    def pay_later(self):
        self.find_element(*point.PAYMENT["pay_later"]).click()
        # elements = self.getElementlist(0, 1, **point.PAYMENT["confirm_container"])
        self.find_element(*point.PAYMENT["later_confirm"]).click()
        # elements[0].click()
        self.back()