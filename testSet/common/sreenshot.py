# -*- coding: utf-8 -*-
import os
import report
from appium import webdriver
today_report_path = report.today_report_path
print today_report_path
# TEMP_FILE = PATH(tempfile.gettempdir() + "/temp.png")
c = 0


class ScreenShot(object):
    def __init__(self, driver):
        # self.driver = ""
        # self.desired_caps = {}
        # self.desired_caps['platformName'] = 'Android'
        # self.desired_caps['platformVersion'] = '4.4.4'
        # self.desired_caps['deviceName'] = 'gucci'
        # self.desired_caps['appPackage'] = 'com.igola.travel'
        # self.desired_caps['appActivity'] = 'com.igola.travel.ui.LaunchActivity'
        # self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', self.desired_caps)
        self.driver = driver

    def get_screenshot(self):
        global c
        self.driver.get_screenshot_as_file(today_report_path + "\\" +str(c) + ".png")
        c += 1

if __name__ == "__main__":

    re = ScreenShot()
    re.get_screenshot()