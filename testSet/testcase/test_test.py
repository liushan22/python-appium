from appium import webdriver
import subprocess
import os
import time

desired_caps ={
    'platformName':'Android',
    'deviceName':'33fd33df',
    'platformVersion':'8.0.0',
    'appPackage':'com.imo.android.imoim',
    'appActivity':'com.imo.android.imoim.activities.Home'
}

cmd = 'appium' + ' -p ' + '4723' + ' --bootstrap-port ' + '4759' + ' -U ' + '33fd33df' + " --session-override"
subprocess.Popen(cmd.decode('gbk'), shell=True)
# os.system(cmd)
time.sleep(10)
webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)