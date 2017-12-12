# -*- coding: utf-8 -*-
from basePage import basePage
import elementConfig as point


class FlightPage(basePage):
    def select_ways(self, way):
        elements = self.getElementlist(**point.FLIGHTPAGE["type_container"])
        elements[way].click()

    def go_citypage(self, city):
        self.find_element(*point.FLIGHTPAGE[city]).click()

    def search(self):
        self.find_element(*point.FLIGHTPAGE["search"]).click()