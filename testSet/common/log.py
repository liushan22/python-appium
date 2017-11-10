# -*- coding: utf-8 -*-

import logging
import os


class logger(object):
    def __init__(self, filepath):
        self.logger = ""
        self.logfile_path = filepath
        log_file = os.path.join(self.logfile_path, "output.log")
        log_level = logging.DEBUG
        self.logger = logging.getLogger("loggingmodule.NomalLogger")
        fh = logging.FileHandler(log_file)
        formatter = logging.Formatter("[%(levelname)s][%(funcName)s][%(asctime)s]%(message)s")
        ch = logging.StreamHandler()
        ch.setLevel(log_level)
        fh.setFormatter(formatter)
        self.logger.addHandler(fh)
        self.logger.addHandler(ch)
        self.logger.setLevel(log_level)

    def getlog(self):
        return self.logger