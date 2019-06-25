import unittest
from . import testcase
from testSet.page.basePage import basePage
from testSet.common.log import logger
import testSet.util.date as date
from testSet.page.loginPage import LoginPage
isinit = False


class IMOTEST(testcase.Testcase):

    def test_login(self):
        page = LoginPage()
        page.access_system()
        page.input_phone_num()
        page.login()


if __name__ == '__main__':
    unittest.main(verbosity=2)