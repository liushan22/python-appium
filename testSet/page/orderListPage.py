# -*- coding: utf-8 -*-
from .basePage import basePage
from . import elementConfig as point


class OrderListPage(basePage):
    def go_order_detail(self):
        element = self.getElementlist(0, 1, **point.OREDER_LIST["order_container"])
        element[0].click()

    def verify_page(self):
        return self.isElement_exist(*point.OREDER_LIST["header"])

