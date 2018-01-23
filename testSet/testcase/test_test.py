import unittest
from testSet.page.homePage import homePage
import testSet.util.date as date
from testSet.common.log import logger
from . import testcase
isinit = False


class test(testcase.Testcase):

    def test_1(self):
        self.log.info("你好")
        self.step1()

    def step1(self):
        self.log.info("hello step")

if __name__ == '__main__':
    unittest.main(verbosity=2)