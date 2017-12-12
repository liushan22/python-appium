from basePage import basePage
import elementConfig as point


class BookingPage(basePage):
    def go_passengerPage(self):
        self.find_element(*point.BOOKING["add_passenger"]).click()

    def go_contactPage(self):
        self.find_element(*point.BOOKING["add_contact"]).click()

    def submit_order(self):
        self.find_element(*point.BOOKING["submit_order"]).click()
