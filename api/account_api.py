# -*- coding: utf-8 -*-
# @Time    : 2022/9/21 11:55
# @Author  : L
# @File    : account_api.py
from common.Request import request
from common.con_method import delete_param


class SubAccount:
    companyId = 17

    def __init__(self, companyId: int):
        self.companyId = companyId
        # self.phone = phone

    # 子账号数据新增/修改
    def operate(self, name: str, phone: str, startDate: str, accountStatus: int, operateType: int, uSubAccountId=None):
        """
        :param uSubAccountId: 子账号id（修改时必填）
        :param phone:手机号码
        :param name:子账号昵称
        :param startDate:开始日期
        :param accountStatus:账号状态 (0:禁用 1:启用)
        :param operateType:操作类型（1.新增 2.修改）
        :return:
        """
        json = {
            "phone": phone,
            "name": name,
            "startDate": startDate,
            "accountStatus": accountStatus,
            "companyId": self.companyId,
            "accountType": 0,
            "companyName": "lansi",
            "operateType": operateType,
            "uSubAccountId": uSubAccountId
        }
        r = request(path='/api/account/operateSubAccount', method='post', data_json=delete_param(json))
        return r.json()

    def query(self, offset=1, limit=20):
        """
        :param offset:页码(int)
        :return:
        """
        params = {"companyId": self.companyId, "offset": offset, "limit": limit}
        r = request(path='/api/account/getSubAccountList', method='get', params=params)
        return r.json()

    # 删除子账号数据
    def delete(self, uSubAccountId):
        """
        :param uSubAccountId: 子账号ID
        :return:
        """
        r = request(path='/api/account/deleteSubAccount', method='DELETE', params={"uSubAccountId": uSubAccountId})
        return r.json()

    # 子账号id
    def find_id(self, phone: str):
        data = self.query()["data"]["items"]
        for i in range(len(data)):
            if data[i]["phone"] == phone:
                id = data[i]["uSubAccountId"]
                return id


# a = SubAccount(16)
#
# print(a.find_id("13761401357"))
