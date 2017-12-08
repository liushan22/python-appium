# -*- coding: utf-8 -*-
import yaml
from page.flightPage import FlightPage
import os
from common.log import logger
import common.report as report
import unittest
import page.elementConfig as point


class GenerateTestcase(unittest.TestCase):
    def setUp(self):
        self.log = logger(report.today_report_path).getlog()
        self.flightPage = FlightPage()

    def findpage(self, page, id):
        pass
        # if page = id

    def get_all_case(self, path_yaml):
        """
        :param path_yaml: testcase adress
        :return: dictionary
        """

        def get_case(path_yaml):
            case_list = []

            inherit_case_file = self.all_file_path("testApp/python-appium/testSet/caselist", ".yaml")
            with open(path_yaml) as f:
                for dic in yaml.load(f):
                    if isinstance(dic, dict):
                        if 'test_inherit' in dic:
                            inherit_case_name = dic['test_inherit']
                            inherit_case = inherit_case_name + '.yaml'
                            if inherit_case in inherit_case_file.keys():
                                case_list += case_list + get_case(inherit_case_file[inherit_case])

                        else:
                            case_list.append(dic)
                    else:
                        self.log.warn('get_case:not dic')
            return case_list

        return get_case(path_yaml)

    def all_file_path(self, root_directory, extension_name):
        """
        :return:
        """
        file_dic = {}
        for parent, dirnames, filenames in os.walk(root_directory):
            for filename in filenames:
                if 'filter' not in filename:
                    if filename.endswith(extension_name):
                        path = os.path.join(parent, filename).replace('\\', '/')
                        file_dic[filename] = path
        return file_dic

    def test_mainflow(self):
        """
        测试用例解释器
        :param path_yaml: 测试用例地址
        1:每执行一条用例会记录下当前的性能
        :return:
        """
        # package_name = ini.get_ini('test_package_name', 'package_name')
        cpu_list = []
        mem_list = []
        path_yaml = "E:\\python\\testApp\python-appium\\testSet\caselist\mainflow.yaml"
        for dic in self.get_all_case(path_yaml):
            self.log.success(str(dic))
            if isinstance(dic, dict):
                if 'test_name' in dic:
                    test_name = str(dic['test_name']).decode('utf-8')
                    self.log.info(
                        'Start the test_case: {}'.format(
                            test_name))
                range_num = 1

                if 'test_range' in dic:
                    # 循环控制
                    # todo:打印循环相关的日志
                    range_num = dic['test_range']

                for i in xrange(0, range_num):
                    if dic['test_action'] == 'click':
                        # 点击
                        test_control_page = "point." + dic['test_control_page']
                        test_control_id = dic['test_control_id']

                        self.log.success('click {}'.format(test_control_id))

                        self.flightPage.find_element(*test_control_page[test_control_id]).click()

                    elif dic['test_action'] == 'send_keys':
                        # 发送文本
                        test_control_page = dic['test_control_page']
                        test_control_id = dic['test_control_id']
                        test_text = dic['test_text']

                        self.log.success('send {} to {}'.format(test_text, test_control))
                        self.flightPage.find_element(*test_control_page[test_control_id])

                    elif 'swipe' in dic['test_action']:
                        # 滑动
                        test_action = dic['test_action']
                        self.log.success('{}'.format(test_action))
                        self.dash_page.swipe_all(test_action)

                    elif 'entity' in dic['test_action']:
                        # 实体按键
                        test_action = dic['test_action']
                        self.log.success('{}'.format(test_action))
                        self.dash_page.send_key_event(test_action)

                    elif dic['test_action'] == 'assert':
                        # 断言
                        test_wait = 15
                        test_control = dic['test_control']
                        test_control_type = dic['test_control_type']
                        test_text = dic['test_text']
                        if dic.has_key('test_wait'):
                            test_wait = int(dic['test_wait'])

                            self.log.success('assert {}'.format(test_control))

                        el = self.dash_page.find_element((test_control_type, test_control), wait=test_wait)
                        assert el.text == test_text

                    if 'test_sleep' in dic:
                        # 等待
                        sleep = dic['test_sleep']
                        self.log.success('Wait {} seconds'.format(sleep))
                        # U.sleep(int(sleep))

                    if True:
                        pass
                        # todo 增加性能的开关判断
                        # U.Logging.success('Obtaining application performance')

                        # cpu = adb.get_cpu(package_name)
                        # mem = adb.get_mem(package_name)
                        # U.Logging.success('cpu:{}'.format(cpu))
                        # U.Logging.success('mem:{}'.format(mem))
                        # cpu_list.append(cpu)
                       #  mem_list.append(mem)

            else:
                self.log.error(
                    'Yaml file format error, the current {}, you need dict'.format(
                        type(dic)))

        # historical_per = self.__select_per(self.filename, self.device, )
        # self.__save_sql(self.filename, self.device, cpu_list, mem_list, 1)
        # if historical_per is not None:
        #     h_cpu = historical_per[0]
        #     h_mem = historical_per[1]
        #     self.__save_cpu_mem(cpu_list, mem_list, h_cpu, h_mem)
        # else:
        #     self.__save_cpu_mem(cpu_list, mem_list, None, None)
        #
        # self.log.success('cpu_list:{}'.format(cpu_list))
        # self.log.success('mem_list:{}'.format(mem_list))
        # return True

    def tearDown(self):
        self.flightPage.quit()



if __name__ == '__main__':
    case = GenerateTestcase()
    case.test_mainflow()