# -*- coding: utf-8 -*-

import os
import unittest
from time import sleep
from common.driver import driver
from selenium.common.exceptions import WebDriverException
import subprocess
import urllib2


# 启动appium
class myServer():
    def __init__(self):
        self.appiumPath = "D:\Appium"

    def run(self):
        print "--------appium server start----------"
        startCMD = "node D:\\Appium\\node_modules\\appium\\bin\\appium.js"
        rootDirection = self.appiumPath[:2]
        # 启动appium
        # os.system(rootDirection + "&" + "cd" + self.appiumPath + "&" + startCMD)
        try:
            subprocess.Popen(rootDirection + "&" + "cd" + self.appiumPath + "&" + startCMD,shell=True)
        except Exception as e:
            print "no"
            raise

    def isServerStart(self):
        try:
            myDriver = driver()
            dr = myDriver.driverConnect()
            if dr:
                return dr
            else:
                return None
        except WebDriverException as e:
            raise

    def quit(self):
        os.system('taskkill /f /im node.exe')
        print "over"







