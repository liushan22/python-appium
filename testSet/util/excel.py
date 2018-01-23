from xlrd import open_workbook
from testSet.util.tran_type import TranType
import os


class Excel:
    def __init__(self, excelName, sheetName):
        parent_path = os.path.abspath(os.path.dirname(os.path.realpath(__file__)))
        caselist_path = os.path.join(os.path.dirname(parent_path), 'caselist')
        self.data = open_workbook(caselist_path + "\\" + excelName + '.xlsx')
        self.table = self.data.sheet_by_name(sheetName)

        # get titles
        self.row = self.table.row_values(0)

        # get rows number
        self.rowNum = self.table.nrows

        # get columns number
        self.colNum = self.table.ncols

        # the current column
        self.curRowNo = 1

    def next(self):
        r = []
        while self.hasNext():
            s = {}
            col = self.table.row_values(self.curRowNo)
            col = TranType().tran_type(*col)
            i = self.colNum
            for x in range(i):
                s[self.row[x]] = col[x]
            r.append(s)
            self.curRowNo += 1
        return r

    def hasNext(self):
        if self.rowNum == 0 or self.rowNum <= self.curRowNo:
            return False
        else:
            return True

    def __generateTestCases(self, testname):
        # parent_path = os.path.abspath(os.path.dirname(os.path.realpath(__file__)))
        caselist_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'caselist')
        data = open_workbook(caselist_path + "\\" + 'test.xlsx')  # 打开文件
        table = data.sheet_by_index(0)  # 遍历所有数据
        # datas = table.row_values(0) # 获取整列数据
        nrows = table.nrows  # 获得行数
        list = []
        for i in range(1, nrows):  # 忽略表头 ，开始遍历
            datas = table.row_values(i)  # 获得每行的数据
            list.append(datas)  # 加载到list中

        # print(list)
        casename = []
        for args in list:
            print(args)
            args = TranType().tran_type(*args)
            setattr(testname, 'test_func_%s' % args[0],
                    testname.getTestFunc(*args))  # 通过setattr自动为TestCase类添加成员方法，方法以“test_func_”开头
            casename.append('test_func_%s' % args[0])
        return casename
