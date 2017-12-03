# -*- coding: utf-8 -*-

from appium import webdriver
import appium
from selenium.common.exceptions import WebDriverException


class driver(object):
    # desired_caps = {
    #     'platformName':'Android',
    #     'platformVersion':'4.4.4',
    #     'deviceName': 'gucci',
    #     'noReset': True,
    #     'appPackage': 'com.igola.travel',
    #     'appActivity':'com.igola.travel.ui.LaunchActivity'
    # }
    def __init__(self, device):
        self.device = device
        self.desired_caps ={}
        self.desired_caps['platformName'] = 'Android'
        self.desired_caps['platformVersion'] = '5.0.2'
        self.desired_caps['udid'] = self.device
        self.desired_caps['deviceName'] = 'hermes'
        self.desired_caps['noReset'] = True
        self.desired_caps['appPackage'] = 'com.igola.travel'
        self.desired_caps['appActivity'] = 'com.igola.travel.ui.LaunchActivity'

    def connect(self, port):
        url = 'http://localhost:%s/wd/hub' % str(port)
        print url
        self.driver = webdriver.Remote(url, self.desired_caps)
        self.log.debug(str(port) + self.device)

    def getDriver(self):
        return self.driver

