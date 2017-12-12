# -*- coding: utf-8 -*-

from selenium.webdriver.common.by import By

HOMEPAGE = {
    "find_flight": (By.ID, "com.igola.travel:id/find_flight_btn"),
    "MY": (By.ID, "com.igola.travel:id/account_btn")
}
FLIGHTPAGE = {
    "search": (By.ID, "com.igola.travel:id/search_btn"),
    "type_container": {
        "type_list": (By.ID, "com.igola.travel:id/trip_type_view"),
        "type": (By.CLASS_NAME, "android.widget.RelativeLayout")
    },
    "depart_city": (By.ID, "com.igola.travel:id/from_city_view"),
    "destination_city": (By.ID, "com.igola.travel:id/to_city_view")
}
TIMELINE = {
    "flight_container": {
        "flight_list": (By.ID, "com.igola.travel:id/results_recycler_view"),
        "flight": (By.CLASS_NAME, "android.widget.RelativeLayout")
    }
}
SUMMARY = {
    "OTA_container": {
        "OTA_list": (By.ID, "com.igola.travel:id/book_list"),
        "OTA": (By.CLASS_NAME, "android.widget.RelativeLayout")
    }
}
BOOKING = {
    "add_passenger": (By.ID, "com.igola.travel:id/add_passenger_layout"),
    "add_contact": (By.ID, "com.igola.travel:id/add_contacts_layout"),
    "submit_order": (By.ID, "com.igola.travel:id/submit_btn")
}
MEMBER_PASSENGER = {
    "passenger_container": {
        "passenger_list": (By.ID, "com.igola.travel:id/passenger_recycler_view"),
        "passenger": (By.ID, "com.igola.travel:id/user_layout"),
    },
    "submit_passenger": (By.ID, "com.igola.travel:id/submit_cv")
}
BOOKING_PASSENGER = {
    "passenger_container": {
        "passenger_list": (By.ID, "com.igola.travel:id/passenger_recycler_view"),
        "zpassenger": (By.ID, "com.igola.travel:id/user_layout"),
        "edit": (By.ID, "com.igola.travel:id/edit_iv"),
        "passenger_type": (By.ID, "com.igola.travel:id/info_tv")
    },
    "submit_passenger": (By.ID, "com.igola.travel:id/submit_btn")
}
BOOKING_CONTACT = {
    "contact_container": {
        "contact_list": (By.ID, "com.igola.travel:id/contact_recycler_view"),
        "contact": (By.ID, "com.igola.travel:id/user_layout")
    },
    "submit_contact": (By.ID, "com.igola.travel:id/submit_btn")
}
LOGIN = {
    "account": (By.ID, "com.igola.travel:id/account_et"),
    "password": (By.ID, "com.igola.travel:id/password_et"),
    "submit": (By.ID, "com.igola.travel:id/login_btn"),
    "error_msg": (By.ID, "com.igola.travel:id/password_error_tv")
}
MY = {
    "login": (By.ID, "com.igola.travel:id/login_btn")
}