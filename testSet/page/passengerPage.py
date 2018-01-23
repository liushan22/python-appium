# -*- coding: utf-8 -*-
from .basePage import basePage
from . import elementConfig as point
import time


class PassengerPage(basePage):
    def submit_passenger(self):
        self.log.info("提交乘机人")
        self.tap("123")
        time.sleep(2)
