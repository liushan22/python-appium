# -*- coding: utf-8 -*-

import os
import unittest
from time import sleep
from driver import driver
from selenium.common.exceptions import WebDriverException
import subprocess
import time
import urllib2


# 启动appium
class myServer():
    def __init__(self):
        self.appiumPath = "D:\Appium"
        # self.appiumPath = "F:\\Appium"

    def run(self):
        """
        启动appium服务
        :return: null
        """
        print "--------appium server start----------"
        startCMD = "node D:\\Appium\\node_modules\\appium\\bin\\appium.js"
        # startCMD = "node Appium\\node_modules\\appium\\bin\\appium.js"
        rootDirection = self.appiumPath[:2]
        # 启动appium
        # os.system(rootDirection + "&" + "cd" + self.appiumPath + "&" + startCMD)
        try:
            subprocess.Popen(rootDirection + "&" + "cd" + self.appiumPath + "&" + startCMD, shell=True)
        except Exception as e:
            print "no"
            raise

    def isServerStart(self):
        try:
            if self.dr:
                return self.dr
            else:
                return None
        except WebDriverException as e:
            raise

    def quit(self):
        """
        退出appium服务
        :return:
        """
        os.system('taskkill /f /im node.exe')
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







