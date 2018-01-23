from ddt import ddt, data, unpack
import testSet.util.excel as excel
from . import testcase
import unittest
from testSet.common.sreenshot import screenshot
from testSet.page.homePage import homePage
from testSet.page.flightPage import FlightPage
from testSet.page.timelinePage import TimelinePage
from testSet.page.summaryPage import SummaryPage
from testSet.page.bookingPage import BookingPage
from testSet.page.bookingDetailPage import BookingDetailPage
from testSet.page.paymentPage import PaymentPage
from testSet.page.orderDetailPage import OrderDetailPage
from testSet.page.orderListPage import OrderListPage

Excel = excel.Excel("flight", "Sheet1")
isinit = False


@ddt
class Test_flight(testcase.Testcase):
    def setUp(self):
        super().setUp()
        self.cabin = ""

    @screenshot
    def step01_go_flightpage(self, expected_result):
        """
        跳转到找飞机页面
        """
        homePage().go_flightPage()

    @screenshot
    def step02_search(self, expected_result):
        """搜索跳转
        """
        flight = FlightPage()
        self.assertTrue(flight.verify_page(), "找机票页面进入错误")
        flight.select_ways(expected_result["type"])
        flight.select_cabin(expected_result["cabin"])
        FlightPage().search()

    @screenshot
    def step03_timeline(self, expected_result):
        """
        验证timeline的航程详情是否正确
        """
        timeline = TimelinePage()
        for type in range(0, int(expected_result["type"])):
            self.assertTrue(timeline.verify_page(), "timeline页面进入错误")
            # actual_result = timeline.get_flight_info()
            # self.assertDictContainsSubset(actual_result, expected_result, "航程详情错误")
            timeline.select_flight(expected_result["price"])

    @screenshot
    def step04_summary(self, expected_result):
        """
        验证summary页面的航程详情是否正确
        :return:
        """
        summary = SummaryPage()
        self.assertTrue(summary.verify_page(), "summary页面进入错误")
        summary.collapse()
        actual_result = summary.get_flight_info(expected_result["type"])
        trips = []
        for trip in expected_result.keys():
            if "trip_type" in trip:
                trips.append(expected_result[trip])
        leg_cabin = summary.check_cabin(expected_result["type"], *trips)
        if isinstance(leg_cabin, tuple):
            for key in leg_cabin[1].keys():
                actual_result[key] = leg_cabin[1][key]
            self.cabin = leg_cabin[0]
        else:
            self.cabin = leg_cabin
        self.assertDictContainsSubset(actual_result, expected_result, "航程详情错误")
        summary.collapse()
        summary.select_ota()

    @screenshot
    def step05_go_booking(self, expected_result):
        """
        验证booking航程详情是否正确
        """
        booking = BookingPage()
        self.assertTrue(booking.verify_page(), "booking页面进入错误")
        self.assertEqual(self.cabin, booking.check_cabin())
        booking.go_detail()

    @screenshot
    def step06_booking_detail(self, expected_result):
        booking_detail = BookingDetailPage()
        self.assertTrue(booking_detail.verify_page(), "booking航程详情页面进入错误")
        actual_result = booking_detail.get_flight_info(expected_result["type"])
        self.assertDictContainsSubset(actual_result, expected_result, "航程详情错误")
        booking_detail.back_to_booking()

    @screenshot
    def step07_submit(self, expected_result):
        booking = BookingPage()
        booking.submit_order()

    @screenshot
    def step08_payment(self, expected_result):
        payment = PaymentPage()
        self.assertTrue(payment.verify_page(), "payment 页面进入错误")
        self.assertEqual(self.cabin, payment.check_cabin())
        payment.pay_later()

    @screenshot
    def step09_go_order(self, expected_result):
        homePage().go_order()
        self.assertTrue(OrderListPage().verify_page(), "订单列表页面进入错误")
        OrderListPage().go_order_detail()

    @screenshot
    def step10_check_order(self, expected_result):
        detail = OrderDetailPage()
        self.assertTrue(detail.verify_page(), "订单详情页面进入错误")
        detail.collapse()
        actual_result = detail.get_flight_info(expected_result["type"])
        self.assertDictContainsSubset(actual_result, expected_result, "航程详情错误")

    def _steps(self):
        for name in sorted(dir(self)):
            if name.startswith("step"):
                yield name, getattr(self, name)

    @data(*Excel.next())
    def test_flights_detail(self, data):
        for name, step in self._steps():
            step(data)


if __name__ == '__main__':
    unittest.main(verbosity=2)
