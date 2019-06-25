# -*- coding: utf-8 -*-
from .basePage import basePage
import elementConfig as point

class LoginPage(basePage):

    def access_system(self):
        try:
            self.find_element(point.system['access']).click()
        except:
            return

    def input_phone_num(self):
        self.send_keys('18819490408', True, True, *point.login['phone_number'])

    def login(self):
        self.find_element(*point.login['login_button']).click()