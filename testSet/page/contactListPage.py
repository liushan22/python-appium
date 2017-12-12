# -*- coding: utf-8 -*-
from basePage import basePage
import time
import elementConfig as point


class ContactListPage(basePage):

    def select_contact(self):
        elements = self.getElementlist(**point.BOOKING_PASSENGER["contact_container"])
        elements[0].click()
        self.find_element(*point.BOOKING_PASSENGER["submit_contact"]).click()
