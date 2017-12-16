# -*- coding: utf-8 -*-
from basePage import basePage
import elementConfig as point


class CityPage(basePage):
    def search_city(self, loc):
        self.log.info("选择%s城市" % loc)
        # self.find_element(*point.CITYPAGE["search_city"]).click()
        self.loc = loc
        self.send_keys(self.loc, True, True, *point.CITYPAGE["search_city"])
        elements = self.getElementlist(**point.CITYPAGE["city_container"])
        isclick = False
        for ele in elements:
            if cmp(ele.text, self.loc):
                ele.click()
                isclick = True
                break
        assert isclick, "未找到该城市"

