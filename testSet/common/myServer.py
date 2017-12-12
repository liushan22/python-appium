# -*- coding: utf-8 -*-

import os
import unittest
from time import sleep
from driver import driver
from selenium.common.exceptions import WebDriverException
import subprocess
import time
import urllib2
import random
import socket
from log import logger
import report


# 启动appium
class myServer(object):
    def __init__(self, device):
        # self.appiumPath = "D:\Appium"
        self.appiumPath = "F:\\Appium"
        self.device = device
        self.log = logger(report.today_report_path).getlog()

    def isOpen(self, ip, port):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            s.connect((ip, int(port)))
            s.shutdown(2)  # shutdown参数表示后续可否读写
            # print '%d is ok' % port
            return True
        except Exception, e:
            return False

    def getport(self):
        port = random.randint(4700, 4900)
        # 判断端口是否被占用
        while self.isOpen('127.0.0.1', port):
            port = random.randint(4700, 4900)
        return port

    def run(self):
        """
        启动appium服务
        :return: null
        """
        aport = self.getport()
        bport = self.getport()
        self.log.info("--------appium server start----------")
        # startCMD = "node D:\\Appium\\node_modules\\appium\\bin\\appium.js"
        # startCMD = "node Appium\\node_modules\\appium\\bin\\appium.js"
        cmd = 'appium' + ' -p ' + str(aport) + ' --bootstrap-port ' + str(bport) + ' -U ' + str(self.device) + " --session-override"
        rootDirection = self.appiumPath[:2]
        # 启动appium
        # os.system(rootDirection + "&" + "cd" + self.appiumPath + "&" + startCMD)
        try:
            subprocess.Popen(rootDirection + "&" + "cd" + self.appiumPath + "&" + cmd, shell=True)
            return aport
        except Exception, msg:
            self.log.error(msg)
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
        self.log.info("----------------appium close---------------------")

if __name__ == '__main__':
    myserver = myServer()
    myserver.run()
    time.sleep(5)
    if myserver.isServerStart():
        print "ok"
    else:
        print "no"
    myserver.quit()







