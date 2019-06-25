# -*- coding: utf-8 -*-

from selenium.webdriver.common.by import By

system = {
    "access": (By.XPATH, "//*[@text='允许']")
}
login = {
    'phone_number' :(By.ID, "com.imo.android.imoim:id/phone"),
    'login_button': (By.ID, "com.imo.android.imoim:id/get_started_button")
}