from basePage import basePage
import elementConfig as point


class SummaryPage(basePage):
    def select_ota(self):
        OTAs = self.getElementlist(**point.SUMMARY["OTA_container"])
        OTAs[0].click()