# -*- coding: utf-8 -*-

from selenium.webdriver.common.by import By

HOMEPAGE = {
    "find_flight": (By.ID, "com.igola.travel:id/find_flight_btn"),
    "MY": (By.ID, "com.igola.travel:id/account_btn"),
    "order": (By.ID, "com.igola.travel:id/order_btn")
}
FLIGHTPAGE = {
    "search": (By.ID, "com.igola.travel:id/search_btn"),
    "type_container": {
        "type_list": (By.ID, "com.igola.travel:id/trip_type_view"),
        "type": (By.CLASS_NAME, "android.widget.RelativeLayout")
    },
    "depart_city": (By.ID, "com.igola.travel:id/from_city_view"),
    "destination_city": (By.ID, "com.igola.travel:id/to_city_view"),
    "cabin": (By.ID, "com.igola.travel:id/seat_class_btn"),
    "confirm": (By.ID, "com.igola.travel:id/confirm_btn")
}
CITYPAGE = {
    "search_city": (By.ID, "com.igola.travel:id/search_city_area"),
    "city_container": {
        "city_list": (By.ID, "com.igola.travel:id/hot_city_rv"),
        "city": (By.ID, "com.igola.travel:id/city_code_tv")
    }
}
TIMELINE = {
    "flight_container": {
        "flight_list": (By.ID, "com.igola.travel:id/results_recycler_view"),
        "flight": (By.ID, "com.igola.travel:id/flight_result_card_view"),
        "code_share": (By.ID, "com.igola.travel:id/code_share_iv"),
        "stop": (By.ID, "com.igola.travel:id/stop_tv"),
        "stopover": (By.ID, "com.igola.travel:id/stopover_iv"),
        "change": (By.NAME, "更换机场"),
        "zprice": (By.ID, "com.igola.travel:id/price_tv")
    },
    "header": (By.ID, "com.igola.travel:id/flights_result_header")
}
SUMMARY = {
    "OTA_container": {
        "OTA_list": (By.ID, "com.igola.travel:id/book_list"),
        "OTA": (By.CLASS_NAME, "android.widget.RelativeLayout"),
        "OTA_cabin": (By.ID, "com.igola.travel:id/class_tv")
    },
    "multi_cabin_container": {
        "cabin_list": (By.ID, "com.igola.travel:id/cabin_lv"),
        "cabin": (By.CLASS_NAME, "android.widget.TextView")
    },
    "retry": (By.ID, "com.igola.travel:id/retry_tv"),
    "collapse": (By.ID, "com.igola.travel:id/collapse_tv"),
    "flight_detail_container": {
        "flight_detail_l_1": (By.ID, "com.igola.travel:id/detail_flight_list_1"),
        "flight_detail_l_2": (By.ID, "com.igola.travel:id/detail_flight_list_2"),
        "flight_detail": (By.ID, "com.igola.travel:id/flight_detail_rl"),
        "transfer": (By.ID, "com.igola.travel:id/transfer_info"),
    },
    "cabin": (By.ID, "com.igola.travel:id/flight_class_tv"),
    "org_terminal": (By.ID, "com.igola.travel:id/org_airport_tv"),
    "dst_terminal": (By.ID, "com.igola.travel:id/dst_airport_tv"),
    "code_share": (By.ID, "com.igola.travel:id/share_code_iv"),
    "stopover": (By.ID, "com.igola.travel:id/flight_stop_tv"),
    "close": (By.ID, "com.igola.travel:id/close_tv")
}
BOOKING = {
    "add_passenger": (By.ID, "com.igola.travel:id/add_passenger_layout"),
    "add_contact": (By.ID, "com.igola.travel:id/add_contacts_layout"),
    "submit_order": (By.ID, "com.igola.travel:id/submit_btn"),
    "add_insurance": (By.ID, "com.igola.travel:id/insurance_header_layout"),
    "add_coupon": (By.ID, "com.igola.travel:id/my_coupons_layout"),
    "title": (By.ID, "com.igola.travel:id/title_tv"),
    "error": (By.CLASS_NAME, "android.widget.Button"),
    "search_other_fight": (By.ID, "com.igola.travel:id/ll1"),
    "flight_detail": (By.ID, "com.igola.travel:id/flight_rl"),
    "cabin": (By.ID, "com.igola.travel:id/total_amount_tv")
}
MEMBER_PASSENGER = {
    "passenger_container": {
        "passenger_list": (By.ID, "com.igola.travel:id/passenger_recycler_view"),
        "passenger": (By.ID, "com.igola.travel:id/user_name_tv"),
    },
    "submit_passenger": (By.ID, "com.igola.travel:id/submit_cv")
}
BOOKING_DETAIL = {
    "header": (By.ID, "com.igola.travel:id/flights_result_header"),
    "flight_detail_container": {
        "flight_detail_l_1": (By.ID, "com.igola.travel:id/detail_flight_list_1"),
        "flight_detail_l_2": (By.ID, "com.igola.travel:id/detail_flight_list_2"),
        "flight_detail": (By.ID, "com.igola.travel:id/flight_detail_rl")
    },
    "cabin": (By.ID, "com.igola.travel:id/flight_class_tv"),
    "org_terminal": (By.ID, "com.igola.travel:id/org_airport_tv"),
    "dst_terminal": (By.ID, "com.igola.travel:id/dst_airport_tv"),
    "transfer": (By.ID, "com.igola.travel:id/transfer_info"),
    "code_share": (By.ID, "com.igola.travel:id/share_code_iv"),
    "stopover": (By.ID, "com.igola.travel:id/flight_stop_tv"),
    "close": (By.ID, "com.igola.travel:id/close_tv")
}
BOOKING_PASSENGER = {
    "passenger_container": {
        "passenger_list": (By.ID, "com.igola.travel:id/passenger_recycler_view"),  # 2
        "passenger": (By.ID, "com.igola.travel:id/user_layout"),  # 0
        "passenger_edit": (By.ID, "com.igola.travel:id/edit_iv"),  # 1
        "passenger_type": (By.ID, "com.igola.travel:id/info_tv"),  # 4
        "passenger_name": (By.ID, "com.igola.travel:id/user_name_tv")  # 3
    },
    "submit_passenger": (By.ID, "com.igola.travel:id/submit_btn")
}
PASSENGER = {
    "title": (By.ID, "com.igola.travel:id/title_tv")
}
BOOKING_CONTACT = {
    "contact_container": {
        "contact_list": (By.ID, "com.igola.travel:id/contact_recycler_view"),
        "contact": (By.ID, "com.igola.travel:id/user_layout")
    },
    "submit_contact": (By.ID, "com.igola.travel:id/submit_btn")
}
BOOKING_INSURANCE = {
    "insurance": (By.ID, "com.igola.travel:id/accident_rv"),
    "submit": (By.ID, "com.igola.travel:id/right_options_btn")
}
BOOKING_COUPON = {
    "coupon_container": {
        "coupon_list": (By.ID, "com.igola.travel:id/coupon_recycler_view"),
        "coupon": (By.ID, "com.igola.travel:id/coupon_card_view")
    }
}
PAYMENT = {
    "payment_container": {
        "payment_list": (By.ID, "com.igola.travel:id/pay_layout"),
        "payment": (By.CLASS_NAME, "android.widget.FrameLayout")
    },
    "pay": (By.ID, "com.igola.travel:id/pay_btn"),
    "third_party_pay": (By.CLASS_NAME, "android.widget.FrameLayout"),
    "third_party_pwd": (By.ID, "com.alipay.android.app:id/spwd_rl_1"),
    "cabin": (By.ID, "com.igola.travel:id/seat_class_tv"),
    "pay_later": (By.ID, "com.igola.travel:id/left_options_btn"),
    "later_confirm": (By.NAME, "稍后付款"),

}
PAYMENT_COMPLETED = {
    "view_orderdetail": (By.ID, "com.igola.travel:id/view_order_btn")
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
ORDER_PASSENGER = {
    "passenger": (By.ID, "com.igola.travel:id/passenger_ll"),
    "type": (By.ID, "com.igola.travel:id/id_type_tv"),
    "id_number": (By.ID, "com.igola.travel:id/id_no_et"),
    "first_name": (By.ID, "com.igola.travel:id/last_name_et"),
    "last_name": (By.ID, "com.igola.travel:id/first_name_et"),
    "gender": (By.ID, "com.igola.travel:id/gender_tv"),
    "birthday": (By.ID, "com.igola.travel:id/birthday_tv"),
    "nationality": (By.ID, "com.igola.travel:id/nationality_tv"),
    "expiration": (By.ID, "com.igola.travel:id/expiration_tv")
}
FEIYA = {
    "search": (By.ID, "com.igola.travel:id/hotel_btn")
}
OREDER_LIST = {
    "order_container": {
        "order_list": (By.ID, "com.igola.travel:id/order_recycler_view"),
        "order": (By.ID, "com.igola.travel:id/order_btn")
    },
    "header": (By.ID, "com.igola.travel:id/expand_lv")
}
ORDER = {
    "collapse": (By.ID, "com.igola.travel:id/collapse_tv"),
    "price": (By.ID, "com.igola.travel:id/price_layout"),
    "flight_detail_container": {
        "flight_detail_l_1": (By.ID, "com.igola.travel:id/detail_flight_list_1"),
        "flight_detail_l_2": (By.ID, "com.igola.travel:id/detail_flight_list_2"),
        "flight_detail": (By.ID, "com.igola.travel:id/flight_detail_rl")
    },
    "cabin": (By.ID, "com.igola.travel:id/flight_class_tv"),
    "org_terminal": (By.ID, "com.igola.travel:id/org_airport_tv"),
    "dst_terminal": (By.ID, "com.igola.travel:id/dst_airport_tv"),
    "transfer": (By.ID, "com.igola.travel:id/transfer_info"),
    "code_share": (By.ID, "com.igola.travel:id/share_code_iv"),
    "stopover": (By.ID, "com.igola.travel:id/flight_stop_tv"),
    "close": (By.ID, "com.igola.travel:id/close_tv"),
}