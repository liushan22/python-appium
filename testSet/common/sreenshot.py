# -*- coding: utf-8 -*-
import os
import time
from log import logger
parent_path=os.path.abspath(os.path.dirname(os.path.realpath(__file__))+os.path.sep+"..")
report_path = os.path.join(os.path.dirname(parent_path), 'result')
today = time.strftime("%Y%m%d", time.localtime(time.time()))
today_report_path = report_path + "\\" + today
# TEMP_FILE = PATH(tempfile.gettempdir() + "/temp.png")
c = 0


class ScreenShot(object):
    def __init__(self, driver):
        self.driver = driver
        self.log = logger(today_report_path).getlog()

    def get_screenshot(self):
        self.log.info("screenshot")
        self.log.info(today_report_path)
        global c
        self.driver.get_screenshot_as_file(today_report_path + "\\" +str(c) + ".png")
        c += 1

if __name__ == "__main__":

    re = ScreenShot()
    re.get_screenshot()