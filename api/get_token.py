# -*- coding: utf-8 -*-
# @Time    : 2022/9/21 11:34
# @Author  : L
# @File    : get_token.py
import pytest

from common.Request import request
import time
import schedule

@pytest.fixture()
def get_token():
    # 调用sendCode接口
    request(path='/api/account/sendCode?mobile=16639051485', method='get')
    # 登录接口
    r = request(path='/api/account/signIn', method='post', data_json={
        "mobile": "16639051485",
        "code": "1234",
        "accountType": 0
    })
    token_data = r.json()['data']['token']

    with open('../config/token.txt', 'w+', encoding='utf-8') as j:
        j.write(token_data)
    return


# 每十分钟执行任务
# schedule.every(10).minutes.do(get_token)
# # 每个小时执行任务
# schedule.every().hour.do(job)
# # 每天的10:30执行任务
# schedule.every().day.at("12:55").do(get_token)
# # 每个月执行任务
# schedule.every().monday.do(job)
# # 每个星期三的13:15分执行任务
# schedule.every().wednesday.at("13:15").do(job)
# # 每分钟的第17秒执行任务
# schedule.every().minute.at(":40").do(get_token)
#
# while True:
#     schedule.run_pending()
#     time.sleep(1)
