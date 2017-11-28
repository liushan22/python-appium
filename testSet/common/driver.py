# -*- coding: utf-8 -*-

from appium import webdriver
from selenium.common.exceptions import WebDriverException


class driver():
    desired_caps = {
        'platformName':'Android',
        'platformVersion':'4.4.4',
        'deviceName': 'gucci',
        'noReset': True,
        'appPackage': 'com.igola.travel',
        'appActivity':'com.igola.travel.ui.LaunchActivity'
    }
    # desired_caps['platformName'] = 'Android'
    # desired_caps['platformVersion'] = '4.4.4'
    # desired_caps['deviceName'] = 'gucci'
    # self.desired_caps['noReset'] = True
    # self.desired_caps['appPackage'] = 'com.igola.travel'
    # self.desired_caps['appActivity'] = 'com.igola.travel.ui.LaunchActivity'
    # self.driver = None

    def connect(self):
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', self.desired_caps)

    def getDriver(self):
        return self.driver

