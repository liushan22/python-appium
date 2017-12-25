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
from page.passengerPage import PassengerPage
from page.orderDetailPage import OrderDetailPage
from page.paymentCompletedPage import PaymentCompletedPage
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
        self.passengerpage = PassengerPage()
        self.orderdetailpage = OrderDetailPage()
        self.paymentcompletepage = PaymentCompletedPage()

    def passenger(self, *args):
        passenger = args[1]
        id = args[2]
        id_type = args[3]
        nationality = args[4]
        gender = args[5]
        print passenger
        self.homepage.go_flightPage()
        self.flightpage.select_ways(0)
        # self.flightpage.go_citypage("depart_city")
        # self.citypage.search_city("CAN")
        time.sleep(1)
        # self.flightpage.go_citypage("destination_city")
        # self.citypage.search_city("LAX")
        self.flightpage.search()
        while True:
            self.timeline.select_flight()
            self.summary.select_ota()
            if not self.booking.find_title():
                continue
            self.booking.go_passengerPage()
            # passenger = ["成人"]
            self.passengerlist.go_passengerpage(passenger)
            self.passengerpage.submit_passenger()
            time.sleep(3)
            self.passengerlist.sumbit_passenger()
            if not self.booking.find_title():
                continue
            # self.booking.go_contactPage()
            # self.contactlist.select_contact()
            # if not self.booking.find_title():
            #     continue
            break
        self.assertTrue(self.booking.find_title())
        # self.booking.submit_order()
        # self.assertTrue(self.paymentpage.find_pay(), "支付页面错误")
        # self.paymentpage.select_payment()
        # self.assertTrue(self.paymentcompletepage.find_btn())
        # self.paymentcompletepage.go_orderdetail()

        # self.orderdetailpage.go_passengerDetail()
        # self.orderdetailpage.check_info(passenger, id_type, id, gender, nationality)

    @staticmethod
    def getTestFunc(*args):
        def func(self):
            self.passenger(*args)

        return func

    def tearDown(self):
        self.homepage.quit()