# -*- coding: utf-8 -*-

import logging
import os
pics = []
picpath = []


class logger(object):
    def __init__(self, filepath):
        self.logger = logging.getLogger('loggingmodule.NomalLogger')
        self.logfile_path = filepath

    def config(self):
        log_file = os.path.join(self.logfile_path, "output.log")
        log_level = logging.INFO
        logging.basicConfig(
            level=logging.DEBUG,
            format='[%(asctime)s][%(process)d:%(thread)d][%(funcName)s][%(levelname)s] %(message)s',
            filename=log_file,
            filemode='a+')
        # self.logger = logging.getLogger('loggingmodule.NomalLogger')
        ch = logging.StreamHandler()
        ch.setLevel(log_level)
        # formatter1 = logging.Formatter('[%(asctime)s][%(process)d:%(thread)d][%(levelname)s] %(message)s')
        # ch.setFormatter(formatter1)
        self.logger.addHandler(ch)

    def getlog(self):
        return self.logger

if __name__ == "__main__":
    l = logger("G:\\")
    l.config()
    log = l.getlog()
    log.info("hi")
    lo = logger("G:\\")
    loga = lo.getlog()
    loga.info("11")
    lo1 = logger("G:\\")
    loga1 = lo.getlog()
    loga1.info("22")