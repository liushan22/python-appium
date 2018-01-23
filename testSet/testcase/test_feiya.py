# -*- coding: utf-8 -*-
import unittest
import testSet.page.elementConfig as point
from appium.webdriver.mobilecommand import MobileCommand
import time
from testSet.page.basePage import basePage
from testSet.page.homePage import homePage
from selenium.webdriver.remote.switch_to import SwitchTo


class Test_feiya(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.homepage = homePage()
        self.basepage = basePage()

    def test_search(self):
        time.sleep(3)
        # element = self.basepage.driver.find_element_by_android_uiautomator("new UiSelector().description(\"搜索\\r\")")
        # element.click()
        ele = self.basepage.driver.find_element_by_android_uiautomator(
            "new UiSelector().className(\"android.support.v7.widget.RecyclerView\")")
        element = ele.find_elements_by_android_uiautomator(
            "new UiSelector().className(\"android.widget.FrameLayout\").clickable(true)")
        element[0].click()
        count = len(element)
        print(count)

        # self.basepage.driver.find_element_by_id("com.igola.travel:id/hotel_btn").click()
        # element = self.basepage.driver.find_element_by_android_uiautomator("new UiSelector().description(\" 搜索酒店\")")
        # element.click()




