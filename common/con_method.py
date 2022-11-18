# -*- coding: utf-8 -*-
# @Time    : 2022/8/17 13:51
# @Author  : L
# @File    : con_method.py
# 定义两个函数，一个内函数，一个外函数


def delete_param(data: dict):
    """删除字典中值为空的键值对"""
    for k in list(data.keys()):
        if not data[k]:
            del data[k]
    return data
