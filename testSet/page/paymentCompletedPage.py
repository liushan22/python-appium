# -*- coding: utf-8 -*-
from basePage import basePage
import elementConfig as point
from testApp.testSet.common.sreenshot import screenshot


class PaymentCompletedPage(basePage):
    def go_orderdetail(self):
        self.log.info("跳转到订单详情")
        self.find_element(*point.PAYMENT_COMPLETED["view_orderdetail"]).click()

    def find_btn(self):
        return self.isElement_exist(*point.PAYMENT_COMPLETED["view_orderdetail"])