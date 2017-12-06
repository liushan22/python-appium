import yaml
import page.flightPage

class GenerateTestcase:
    def __init__(self):
        pass

    def get_all_case(self, path_yaml):
        """
        :param path_yaml: 用例地址
        :return: 返回yaml内字典,且遍历继承的信息,支持多重继承
        """
        def get_case(path_yaml):
            case_list = []

            inherit_case_file = public.GetCase.case_yaml_file()
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
                        U.Logging.warn('get_case:not dic')
            return case_list

        return get_case(path_yaml)