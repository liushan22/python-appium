# -*- coding: utf-8 -*-
import unittest
import time
from common.log import logger
import common.report as report
from page.homePage import homePage
from page.flightPage import FlightPage
from page.timelinePage import TimelinePage
from page.summaryPage import SummaryPage
from page.bookingPage import BookingPage
from page.passengerListPage import passengerListPage
from page.contactListPage import ContactListPage
from page.cityPage import CityPage
from page.insurancePage import InsurancePage
from page.couponPage import CouponPage
from common.sreenshot import screenshot
from page.paymentPage import PaymentPage
import page.elementConfig as point
isinit = False


class Test_Passenger(unittest.TestCase):
    def setUp(self):
        l = logger(report.today_report_path)
        global isinit
        if not isinit:
            l.config()
            isinit = True
        self.log = l.getlog()
        self.log.info("test_passenger")
        self.homepage = homePage()
        self.flightpage = FlightPage()
        self.timeline = TimelinePage()
        self.summary = SummaryPage()
        self.booking = BookingPage()
        self.passengerlist = passengerListPage()
        self.contactlist = ContactListPage()
        self.citypage = CityPage()
        self.insurancepage = InsurancePage()
        self.couponpage = CouponPage()
        self.paymentpage = PaymentPage()

    def passenger(self, *args):
        passenger = args[1]
        print passenger
        self.homepage.go_flightPage()
        self.flightpage.select_ways(0)
        self.flightpage.go_citypage("depart_city")
        self.citypage.search_city("CAN")
        time.sleep(1)
        self.flightpage.go_citypage("destination_city")
        self.citypage.search_city("LAX")
        self.flightpage.search()
        #for i in range(0, trip_type+1):
        self.timeline.select_flight()
        self.summary.select_ota()
        time.sleep(1)

        self.booking.find_title()
        self.booking.go_passengerPage()
        # passenger = ["成人"]
        self.passengerlist.select_passenger(passenger)

        self.booking.find_title()
        self.booking.go_contactPage()
        self.contactlist.select_contact()
        self.booking.find_title()

        # self.booking.submit_order()
        # self.assertTrue(self.paymentpage.isElement_exist(*point.PAYMENT["pay"]))

    @staticmethod
    def getTestFunc(*args):
        def func(self):
            self.passenger(*args)

        return func

    def tearDown(self):
        self.homepage.quit()