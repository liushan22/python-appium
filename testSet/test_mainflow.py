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
        self.citypage = CityPage()
        self.insurancepage = InsurancePage()
        self.couponpage = CouponPage()
        self.paymentpage = PaymentPage()

    def mainflow(self, *args):
        trip_type = int(args[2])
        depart_city = args[3]
        destination_city = args[4]
        passengers = args[5]
        passenger_type = []
        passenger_1 = passengers[0:6]
        passenger_type.append(passenger_1)
        insurance = args[6]
        coupon = args[7]
        if len(passengers) > 6:
            passenger_2 = passengers[7:13]
            passenger_type.append(passenger_2)
        self.homepage.go_flightPage()
        self.flightpage.select_ways(trip_type)
        self.flightpage.go_citypage("depart_city")
        self.citypage.search_city(depart_city)
        time.sleep(1)
        self.flightpage.go_citypage("destination_city")
        self.citypage.search_city(destination_city)
        self.flightpage.search()
        for i in range(0, trip_type+1):
            self.timeline.select_flight()
        self.summary.select_ota()
        time.sleep(1)

        self.booking.find_title()
        self.booking.go_passengerPage()
        self.passengerlist.select_passenger(*passenger_type)

        self.booking.find_title()
        self.booking.go_contactPage()
        self.contactlist.select_contact()
        self.booking.find_title()

        if insurance == "1":
            self.booking.go_insurance()
            self.insurancepage.select_insur()
        self.booking.find_title()

        if coupon == "1":
            self.booking.go_couponPage()
            self.couponpage.select_coupon()
        self.booking.submit_order()
        self.paymentpage.select_payment()

    @staticmethod
    def getTestFunc(*args):
        def func(self):
            self.mainflow(*args)

        return func

    def tearDown(self):
        self.homepage.quit()