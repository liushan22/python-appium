# -*- coding: utf-8 -*-
from .basePage import basePage
from . import elementConfig as point


class CouponPage(basePage):
    def select_coupon(self):
        self.log.info("选择优惠券")
        element = self.getElementlist(**point.BOOKING_COUPON["coupon_container"])
        element[0].click()