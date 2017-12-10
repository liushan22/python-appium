# -*- coding: utf-8 -*-

import logging
import os
pics = []
picpath = []


class logger(object):
    def __init__(self, filepath):
        # self.logger = ""
        self.logfile_path = filepath
        log_file = os.path.join(self.logfile_path, "output.log")
        log_level = logging.DEBUG
        # self.logger = logging.getLogger("loggingmodule.NomalLogger")
        # fh = logging.FileHandler(log_file)
        # formatter = logging.Formatter("[%(levelname)s][%(funcName)s][%(asctime)s]%(message)s")
        # ch = logging.StreamHandler()
        # ch.setLevel(log_level)
        # fh.setFormatter(formatter)
        # self.logger.addHandler(fh)
        # self.logger.addHandler(ch)
        # self.logger.setLevel(log_level)
        logging.basicConfig(
            level=logging.DEBUG,
            format='[%(asctime)s][%(process)d:%(thread)d][%(funcName)s][%(levelname)s] %(message)s',
            filename=log_file,
            filemode='a+')
        self.logger = logging.getLogger('loggingmodule.NomalLogger')
        #if not self.logger.handlers:

        ch = logging.StreamHandler()
        ch.setLevel(log_level)
        # formatter1 = logging.Formatter('[%(asctime)s][%(process)d:%(thread)d][%(levelname)s] %(message)s')
        # ch.setFormatter(formatter1)
        self.logger.addHandler(ch)

    def getlog(self):
        return self.logger

if __name__ == "__main__":
    l = logger("E:\\").getlog()
    l.info("hi")
    l.info("hello")
    l.info("hello,world")