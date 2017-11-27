# -*- coding: utf-8 -*-

from selenium.webdriver.common.by import By

HOMEPAGE = {
    "find_flight": (By.ID, "com.igola.travel:id/find_flight_btn")
}
FLIGHTPAGE = {
    "search": (By.ID, "com.igola.travel:id/search_btn")
}
TIMELINE = {
    "flight_list": (By.ID, "com.igola.travel:id/results_recycler_view"),
    "flight": (By.CLASS_NAME, "android.widget.RelativeLayout")
}
SUMMARY = {
    "OTA_list": (By.ID, "com.igola.travel:id/book_list"),
    "OTA": (By.CLASS_NAME, "android.widget.RelativeLayout")
}
BOOKING = {
    "passenger_list": (By.ID, "com.igola.travel:id/passenger_recycler_view"),
    "passenger":(By.ID, "com.igola.travel:id/user_layout"),
    "add_passenger": (By.ID, "com.igola.travel:id/add_passenger_layout"),
    "submit_passenger": (By.ID, "com.igola.travel:id/submit_cv")
}
MEMBER_PASSENGER = {
    "passenger_list": (By.ID, "com.igola.travel:id/passenger_recycler_view"),
    "passenger":(By.ID, "com.igola.travel:id/user_layout"),
    "submit_passenger": (By.ID, "com.igola.travel:id/submit_cv")
}