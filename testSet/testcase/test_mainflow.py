# -*- coding: utf-8 -*-
import unittest
import time
from testSet.common.log import logger
import testSet.common.report as report
from testSet.page.homePage import homePage
from testSet.page.flightPage import FlightPage
from testSet.page.timelinePage import TimelinePage
from testSet.page.summaryPage import SummaryPage
from testSet.page.bookingPage import BookingPage
from testSet.page.passengerListPage import passengerListPage
from testSet.page.contactListPage import ContactListPage
from testSet.page.cityPage import CityPage
from testSet.page.insurancePage import InsurancePage
from testSet.page.couponPage import CouponPage
from testSet.common.sreenshot import screenshot
from testSet.page.paymentPage import PaymentPage
import testSet.page.elementConfig as point


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
        while True:
            for i in range(0, trip_type + 1):
                self.timeline.select_flight()
            self.summary.select_ota()
            time.sleep(1)
            if not self.booking.verify_page():
                continue
            self.booking.go_passengerPage()
            self.passengerlist.select_passenger(*passenger_type)
            if not self.booking.verify_page():
                continue
            self.booking.go_contactPage()
            self.contactlist.select_contact()
            if not self.booking.verify_page():
                continue

            if insurance == "1":
                self.booking.go_insurance()
                self.insurancepage.select_insur()
            if not self.booking.verify_page():
                continue

            if coupon == "1":
                self.booking.go_couponPage()
                self.couponpage.select_coupon()
            if not self.booking.isElement_clickable(*point.BOOKING["submit_order"]):
                continue
            break
        self.booking.submit_order()
        self.paymentpage.select_payment()

    @staticmethod
    def getTestFunc(*args):
        def func(self):
            self.mainflow(*args)

        return func

    def tearDown(self):
        self.homepage.quit()