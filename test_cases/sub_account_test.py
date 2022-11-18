# -*- coding: utf-8 -*-
# @Time    : 2022/9/22 9:26
# @Author  : L
# @File    : sub_account_test.py
import allure

from api.account_api import SubAccount
from api.get_token import get_token


class TestSubAccount:
    def setup_class(self):
        self.sub_account = SubAccount(16)
        # 判断是否存在该账户，如果存在清理
        create_id = self.sub_account.find_id('13761401357')
        if create_id:
            self.sub_account.delete(create_id)

    @allure.story("新增子账号")
    def test_add(self):
        result = self.sub_account.operate('测试1', '13761401357', '2030-07-12', 1, 1)
        assert result["code"] == 2000
        assert result["data"]["state"] is True
        assert result["msg"] == "SUCCESS"

        # 验证是否新增成功
        assert self.sub_account.find_id('13761401357') is not None

    @allure.story("查询新增子账号信息")
    def test_query(self):
        result = self.sub_account.query()["data"]["items"]
        for i in range(len(result)):
            if result[i]["phone"] == '13761401357':
                assert result[i]["name"] == '测试1'
                assert result[i]["startDate"] == '2030-07-12'
                assert result[i]["accountStatus"] == '1'
                assert result[i]["companyId"] == 16

    @allure.story("查询新增子账号信息")
    def test_delete(self):
        with allure.step("找到子账号id"):
            my_delete_id = self.sub_account.find_id('13761401357')

        with allure.step("调用删除接口"):
            result = self.sub_account.delete(my_delete_id)
        assert result["code"] == 2000
        assert result["data"]["state"] is True
        assert result["msg"] == "SUCCESS"
        # 验证是否删除成功
        assert self.sub_account.find_id('13761401357') is None

    @allure.story("修改子账号")
    def test_update(self):
        my_update_id = self.sub_account.find_id('16639051485')
        result = self.sub_account.operate('测试2', '16639051485', '2022-07-13', 1, 2, my_update_id)
        assert result["code"] == 2000
        assert result["data"]["state"] is True
        assert result["msg"] == "SUCCESS"
