# -*- coding: utf-8 -*-
# @Time    : 2022/8/17 9:50
# @Author  : L
# @File    : Log.py
import logging
import os


def get_logger():
    # create logger
    logger = logging.getLogger(os.path.basename(__file__))
    logger.setLevel(logging.DEBUG)
    # create console handler and set level to debug
    ch = logging.FileHandler(filename='../logs/mylog.log', encoding="utf-8")
    ch.setLevel(logging.DEBUG)
    # create formatter
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    # add formatter to ch
    ch.setFormatter(formatter)
    # add ch to logger
    logger.addHandler(ch)
    return logger


logger = get_logger()


