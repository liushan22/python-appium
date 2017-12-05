#!/user/bin python
# -*- coding:utf-8 -*-
'''
  涉及的命令：http://developer.android.com/tools/help/adb.html#wireless
        adb devices     # 查看已经连接的设备
        adb shell netcfg    #（查看设备 IP）
        adb tcpip 555  # Restart host adb in tcpip mode.
        adb connect # Connect adb host to device
        adb devices
'''

import subprocess as sp
import os
import sys
import time
import re
# add one


def main():
    # print("main")
    cmd_devices = 'adb devices'
    cmd_cfg = 'adb -s %s shell netstat'
    cmd_tcpip = 'adb -s %s tcpip 5555'
    cmd_conn = 'adb connect %s '
    # info_devices = sp.Popen(cmd_devices,shell=True)
    src_outer = os.popen(cmd_devices).read().strip()
    # info_devices = sp.call(cmd_devices)
    # print("---------")
    # print(info_devices)
    # print("src_outer" , src_outer)
    if not src_outer:
        print('there is no message out when cmd ' + cmd_devices)
        sys.exit(0)
    touch_info = 'List of devices attached'
    lists = src_outer[src_outer.index(touch_info) + len(touch_info):]

    if not lists:
        print("There has no device connect ths computer ! ")
        sys.exit(0)
        # print(lists)
    dev_list = lists.strip().split('\n')
    # print(dev_list)
    if dev_list and len(dev_list) >= 1:
        for device in dev_list:
            print(device)
            if '5555' in device:
                break
            dev_name = device.split('\t')[0]
            print(dev_name)
            tcpip_info = os.popen(cmd_tcpip % dev_name).read().strip()
            print((cmd_tcpip % dev_name), tcpip_info)
            time.sleep(3)
            cfg_info = os.popen(cmd_cfg % dev_name).read().strip().split('\n')
            if not cfg_info:
                print('adb shell cfg command run error ')
                sys.exit(0)
            wlan = 'wlan'
            # for cfg in cfg_info:
            #
            #     iter_cfg = cfg.strip()
            #     if iter_cfg.startswith(wlan):
            #         # print('iter_cfg' , iter_cfg)
            #         ips = iter_cfg.split(' ')[-4]
            #         ip = ips[:ips.index('/')]
            #         # print("ip-->" , ip)
            #         conn_info = os.popen(cmd_conn % ip).read().strip()
            #         print((cmd_conn % ip), conn_info)
            cfg = cfg_info[2]
            pattern = re.compile("((?:(?:25[0-5]|2[0-4]\d|((1\d{2})|([1-9]?\d)))\.){3}(?:25[0-5]|2[0-4]\d|((1\d{2})|([1-9]?\d))))")
            ip = re.findall(pattern, cfg)
            # ip = cfg[(cfg.index(" 1")-1):cfg.index(':')].strip()
            print("ip-->", ip[0][0])
            conn_info = os.popen(cmd_conn % ip[0][0]).read().strip()
            print((cmd_conn % ip[0][0]), conn_info)
                    # pass

                    # print(cfg_info)


if __name__ == '__main__':
    main()
