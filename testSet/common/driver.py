# -*- coding: utf-8 -*-

from appium import webdriver
from .log import logger
from . import report
import os
import testSet.util.date as date
import appium
from selenium.common.exceptions import WebDriverException
dr = webdriver.Remote


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
        self.desired_caps['platformVersion'] = '8.0.0'
        self.desired_caps['udid'] = self.device
        self.desired_caps['deviceName'] = 'hermes'
        self.desired_caps['noReset'] = True
        self.desired_caps['appPackage'] = 'com.imo.android.imoim' # com.imo.android.imoimalpha; com.imo.android.imoimlite
        self.desired_caps['appActivity'] = 'com.imo.android.imoim.activities.Home'
        # self.desired_caps['nativeWebTap'] = True
        self.log = logger(date.today_report_path).getlog()

    def connect(self, port):
        url = 'http://127.0.0.1:%s/wd/hub' % str(port)
        self.log.debug(url)
        try:
            global dr
            dr = webdriver.Remote(url, self.desired_caps)
            self.log.debug("启动接口为：%s,手机ID为：%s" % (str(port), self.device))
        except Exception:
            self.log.info("appium 启动失败")
            os.popen("taskkill /f /im adb.exe")
            raise

    def getDriver(self):
        return dr

