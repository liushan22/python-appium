# -*- coding: utf-8 -*-
import os
import time
import log
from driver import driver
parent_path=os.path.abspath(os.path.dirname(os.path.realpath(__file__))+os.path.sep+"..")
report_path = os.path.join(os.path.dirname(parent_path), 'result')
today = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
today_report_path = report_path + "\\image"
# TEMP_FILE = PATH(tempfile.gettempdir() + "/temp.png")


    # def __init__(self, func):
    #     # self.driver = driver
    #     self.func = func
    #     self.log = logger(today_report_path).getlog()
def adb_screenshot(self):
    self.log.info(today_report_path)
    picname = today + ".png"
    PATH = lambda p: os.path.abspath(p)
    os.popen("adb wait-for-device")
    os.popen("adb shell screencap -p /data/local/tmp/tmp.png")
    os.popen("adb pull /data/local/tmp/tmp.png " + PATH(today_report_path + "/" + picname))
    self.log.info("screenshot:" + picname + " ")
    os.popen("adb shell rm /data/local/tmp/tmp.png")


def screenshot(func):
    def inner(self, *args, **kwargs):
        try:
            #f = func(self, *args, **kwargs)
            return func(self, *args, **kwargs)
        except AssertionError as e:
            self.log.error("断言错误")
            adb_screenshot(self)
            raise
        except AttributeError:
            adb_screenshot(self)
            self.log.info("%s 页面没有找到%s元素" % (self, loc))
        except Exception, msg:
            self.log.error("其他出错:%s" % msg)
            adb_screenshot(self)
            raise
    return inner




# if __name__ == "__main__":
#
#     re = ScreenShot()
    # re.get_screenshot()