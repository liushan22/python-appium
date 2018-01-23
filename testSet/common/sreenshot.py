# -*- coding: utf-8 -*-
import os
import time
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
import testSet.util.date as date


def adb_screenshot(self):
    today_report_path = date.report_path + "\\image"
    today = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
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
            return func(self, *args, **kwargs)
        except AssertionError as e:
            self.log.error("断言错误")
            adb_screenshot(self)
            self.fail("{} failed ({}: {})".format(func.__name__, type(e), e))
        except (NoSuchElementException, TimeoutException) as msg:
            adb_screenshot(self)
            self.log.info("页面没有找到元素%s" % msg)
            raise
        except Exception as msg:
            self.log.error("其他出错:%s" % msg)
            adb_screenshot(self)
            raise
    return inner



