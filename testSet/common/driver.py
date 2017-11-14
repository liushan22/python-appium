# -*- coding: utf-8 -*-

from appium import webdriver
from selenium.common.exceptions import WebDriverException
driver = ""


class driver():
    def __init__(self):
        self.desired_caps = {}
        self.desired_caps['platformName'] = 'Android'
        self.desired_caps['platformVersion'] = '4.4.4'
        self.desired_caps['deviceName'] = 'gucci'
        self.desired_caps['noReset'] = True
        self.desired_caps['appPackage'] = 'com.igola.travel'
        self.desired_caps['appActivity'] = 'com.igola.travel.ui.LaunchActivity'

    def driverConnect(self):
        global driver
        try:
            driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', self.desired_caps)
            return driver
        except WebDriverException as e:
            raise
