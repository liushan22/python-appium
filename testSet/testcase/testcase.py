import unittest
import testSet.util.date as date
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
from testSet.page.paymentPage import PaymentPage
from testSet.page.passengerPage import PassengerPage
from testSet.page.orderDetailPage import OrderDetailPage
from testSet.page.paymentCompletedPage import PaymentCompletedPage
from ddt import ddt
isinit = False


@ddt
class Testcase(unittest.TestCase):

    def setUp(self):
        l = logger(date.today_report_path)
        global isinit
        if not isinit:
            l.config()
            isinit = True
        self.log = l.getlog()
        self.homepage = homePage()

    def tearDown(self):
        self.homepage.quit()
