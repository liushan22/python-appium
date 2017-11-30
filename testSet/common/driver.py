# -*- coding: utf-8 -*-

from appium import webdriver
from selenium.common.exceptions import WebDriverException


class driver():
    # desired_caps = {
    #     'platformName':'Android',
    #     'platformVersion':'4.4.4',
    #     'deviceName': 'gucci',
    #     'noReset': True,
    #     'appPackage': 'com.igola.travel',
    #     'appActivity':'com.igola.travel.ui.LaunchActivity'
    # }
    def __init__(self):
        self.desired_caps ={}
        self.desired_caps['platformName'] = 'Android'
        self.desired_caps['platformVersion'] = '5.0.2'
        self.desired_caps['deviceName'] = 'hermes'
        self.desired_caps['noReset'] = True
        self.desired_caps['appPackage'] = 'com.igola.travel'
        self.desired_caps['appActivity'] = 'com.igola.travel.ui.LaunchActivity'

    def connect(self):
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', self.desired_caps)

    def getDriver(self):
        return self.driver

