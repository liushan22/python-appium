# -*- coding: utf-8 -*-
import os
import time
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
import traceback
import sys
import log
from driver import driver
parent_path=os.path.abspath(os.path.dirname(os.path.realpath(__file__))+os.path.sep+"..")
report_path = os.path.join(os.path.dirname(parent_path), 'result')
today = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
today_report_path = report_path + "\\image"
# TEMP_FILE = PATH(tempfile.gettempdir() + "/temp.png")
reload(sys)
sys.setdefaultencoding('utf8')


    # def __init__(self, func):
    #     # self.driver = driver
    #     self.func = func
    #     self.log = logger(today_report_path).getlog()
def adb_screenshot(self):
    self.log.debug(today_report_path)
    picname = today + ".png"
    PATH = lambda p: os.path.abspath(p)
    os.popen("adb wait-for-device")
    os.popen("adb shell screencap -p /data/local/tmp/tmp.png")
    os.popen("adb pull /data/local/tmp/tmp.png " + PATH(today_report_path + "/" + picname))
    self.log.info("screenshot:" + picname + " ")
    os.popen("adb shell rm /data/local/tmp/tmp.png")
    time.sleep(1)


def screenshot(func):
    def inner(self, *args, **kwargs):
        try:
            #f = func(self, *args, **kwargs)
            return func(self, *args, **kwargs)
        except AssertionError as e:
            self.log.error("断言错误")
            adb_screenshot(self)
            # s = traceback.format_exc()
            # self.log.error(s.decode("utf-8", errors='ignore'))
            raise
        except (NoSuchElementException, TimeoutException), msg:
            adb_screenshot(self)
            self.log.info("页面没有找到元素%s" % msg)
            # s = traceback.format_exc()
            # self.log.error(s.decode("utf-8", errors='ignore'))
            raise
        except Exception, msg:
            self.log.error("其他出错:%s" % msg)
            adb_screenshot(self)
            # s = traceback.format_exc()
            # self.log.error(s.decode("utf-8", errors='ignore'))
            raise
    return inner


def testcase_exception(func):
    def inner(self, *args, **kwargs):
        try:
            # f = func(self, *args, **kwargs)
            return func(self, *args, **kwargs)
        except:
            # s = traceback.format_exc()
            # self.log.error(s.decode("utf-8", errors='ignore'))
            raise
    return inner



# if __name__ == "__main__":
#
#     re = ScreenShot()
    # re.get_screenshot()