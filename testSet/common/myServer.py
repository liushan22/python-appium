# -*- coding: utf-8 -*-

import os
import unittest
from time import sleep
import driver
from selenium.common.exceptions import WebDriverException
import subprocess
import time
import urllib2


# 启动appium
class myServer():
    def __init__(self):
        self.appiumPath = "D:\Appium"
        self.dr = driver.driver

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
            self.dr = driver.driver().driverConnect()
            if self.dr:
                return True
            else:
                return False
        except WebDriverException as e:
            raise

    def quit(self):
        os.system('taskkill /f /im node.exe')
        self.dr.quit()
        print "over"

if __name__ == '__main__':
    myserver = myServer()
    myserver.run()
    time.sleep(5)
    if myserver.isServerStart():
        print "ok"
    else:
        print "no"
    myserver.quit()







