# -*- coding: utf-8 -*-
import unittest
from common.log import logger
import common.report as report
from page.homePage import homePage
from page.flightPage import FlightPage
from page.timelinePage import TimelinePage
from page.summaryPage import SummaryPage
from page.bookingPage import BookingPage
from page.passengerListPage import passengerListPage
from page.contactListPage import ContactListPage


class Test_Mainfolw(unittest.TestCase):
    def setUp(self):
        self.log = logger(report.today_report_path).getlog()
        self.log.info("test_mainflow")
        self.homepage = homePage()
        self.flightpage = FlightPage()
        self.timeline = TimelinePage()
        self.summary = SummaryPage()
        self.booking = BookingPage()
        self.passengerlist = passengerListPage()
        self.contactlist = ContactListPage()

    def test_mainflow(self):
        self.homepage.go_flightPage()
        self.flightpage.select_ways(0)
        self.flightpage.search()
        self.timeline.select_flight()
        self.summary.select_ota()
        self.booking.go_passengerPage()
        passenger_type = ["成人"]
        self.passengerlist.select_passenger(passenger_type)
        self.booking.go_contactPage()
        self.contactlist.select_contact()
        self.booking.submit_order()

    @staticmethod
    def getTestFunc(arg1, arg2, arg3, arg4):
        def func(self):
            self.mainflow(arg1, arg2, arg3, arg4)

        return func

    def tearDown(self):
        self.homepage.quit()