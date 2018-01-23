import os
import time


parent_path = os.path.abspath(os.path.dirname(os.path.realpath(__file__))+os.path.sep+"..")
report_path = os.path.join(os.path.dirname(parent_path), 'result')
today = time.strftime("%Y%m%d", time.localtime(time.time()))
today_report_path = report_path + "\\" + today
print(today_report_path)