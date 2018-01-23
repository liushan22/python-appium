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
from testSet.page.passengerPage import PassengerPage
from testSet.page.orderDetailPage import OrderDetailPage
from testSet.page.paymentCompletedPage import PaymentCompletedPage
import testSet.page.elementConfig as point


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
        print(passenger)
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
            title = self.booking.verify_page()
            if not title:
                continue
            elif title == "ota":
                self.summary.select_ota()
            self.booking.go_passengerPage()
            # passenger = ["成人"]
            self.passengerlist.go_passengerpage(passenger)
            self.passengerpage.submit_passenger()
            time.sleep(3)
            self.passengerlist.sumbit_passenger()
            # if not self.booking.find_title():
            #     continue
            # self.booking.go_contactPage()
            # self.contactlist.select_contact()
            # if not self.booking.find_title():
            #     continue
            break
        self.assertTrue(self.booking.verify_page())
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