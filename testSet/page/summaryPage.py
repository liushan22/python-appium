# -*- coding: utf-8 -*-
from basePage import basePage
import elementConfig as point


class SummaryPage(basePage):
    def select_ota(self):
        self.log.info(u"选择 ota")
        OTAs = self.getElementlist(**point.SUMMARY["OTA_container"])
        OTAs[0].click()