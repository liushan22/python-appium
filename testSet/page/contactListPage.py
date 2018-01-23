# -*- coding: utf-8 -*-
from .basePage import basePage
import time
from . import elementConfig as point


class ContactListPage(basePage):

    def select_contact(self):
        self.log.info("选择联系人")
        elements = self.getElementlist(**point.BOOKING_CONTACT["contact_container"])
        elements[0].click()
        self.tap("123")
