# -*- coding: utf-8 -*-
from basePage import basePage
import elementConfig as point
import time
from testSet.common.sreenshot import screenshot


class PaymentPage(basePage):
    @screenshot
    def select_payment(self):
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