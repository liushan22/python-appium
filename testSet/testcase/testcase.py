import unittest
import testSet.util.date as date
from testSet.common.log import logger
import testSet.common.report as report
from testSet.page.basePage import basePage
from ddt import ddt
isinit = False


@ddt
class Testcase(unittest.TestCase):

    def setUp(self):
        l = logger(date.today_report_path)
        global isinit
        if not isinit:
            l.config()
            isinit = True
        self.log = l.getlog()
        self.basepage = basePage()

    def tearDown(self):
        self.basepage.quit()
