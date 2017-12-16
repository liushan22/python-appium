# -*- coding: utf-8 -*-
from basePage import basePage
import elementConfig as point


class InsurancePage(basePage):
    def select_insur(self):
        self.find_element(*point.BOOKING_INSURANCE["insurance"]).click()
        self.submit_insur()

    def submit_insur(self):
        self.find_element(*point.BOOKING_INSURANCE["submit"]).click()