# -*- coding: utf-8 -*-
# @Time    : 2022/8/1 13:49
# @Author  : L
# @File    : Request.py

import hashlib
import json
import time
import uuid
import hmac
import base64
import requests
import urllib3

"""
公共业务封装 哪个文件报错了
"""


def request(path, method, params=None, data=None, data_json=None):
    '''
    阿里云网关请求方法
    :param path: 请求路径 (不包括域名)
    :param method: 请求方式 get/post
    :param params: get请求中query参数
    :param data: post请求里的body参数
    :return: 响应
    '''

    if data_json is None:
        data_json = {}
    if params is None:
        params = {}
    if data is None:
        data = {}
    # 域名
    # host = 'managedvlpapi.realtynavi.com'
    host = 'citymapapi.realtynavi.com'
    # 阿里云应用  key
    key = '204105816'
    # 阿里云应用  密钥
    secret = '9FDMXbZl0SFQgfb6P5EajbYFtpqh8eoh'
    # http协议
    channel = 'http'
    # token
    with open('../config/token.txt', 'r', encoding='utf-8') as j:
        token = j.read()
        j.close()
    # Content_MD5
    if data_json:
        md5_json = hashlib.md5(json.dumps(data_json).encode('utf-8')).digest()
        str64 = base64.b64encode(md5_json)
        md5 = str(str64, encoding='utf-8')
    else:
        md5 = ''

    # 初始化请求头
    headers = {
        "Host": host,
        "X-Ca-Timestamp": str(int(time.time() * 1000)),
        "gateway_channel": channel,
        "X-Ca-Request-Mode": "debug",
        "X-Ca-Key": key,
        "X-Ca-Stage": 'TEST',  # 'RELEASE'正式 & 'TEST'测试
        "X-Ca-Nonce": str(uuid.uuid1()),
        "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8" if data else "application/json;charset=UTF-8",
        "X-Ca-Signature-Headers": "X-Ca-Timestamp,X-Ca-Request-Mode,X-Ca-Key,X-Ca-Stage",
        "X-Ca-Signature": "",
        "Content-MD5": md5,
        # "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJhY2NvdW50SWQiOjMyLCJzZXJpYWxWZXJzaW9uVUlEIjoiNzY2NzUyNzE4NzMyMTE1MDUzMiIsIm5pY2tOYW1lIjoi5p2O6ZuvIiwiYWNjb3VudElkZW50aWZpZXIiOiIzMiIsImV4cCI6MTY2MzIwNjI1NywianRpIjoiODY2YzlmMzk2YmM0NDJmOWExZTY2ODkyZGYyMTdjYjYiLCJwbGF0Zm9ybSI6IlBDX0Jyb3dzZXIifQ.LQKUObFRG7adYDT8O0udBnc9bbBIZg3BETnXQFp-AT4"
        "token": token
    }
    # 参与签名的参数
    HTTPMethod = method.upper()
    Accept = '*/*'
    Content_MD5 = headers['Content-MD5']
    Content_Type = headers['Content-Type']
    Date = ''
    Headers = ''
    Headers += 'X-Ca-Key:{}\n'.format(headers['X-Ca-Key'])
    Headers += 'X-Ca-Request-Mode:{}\n'.format(headers['X-Ca-Request-Mode'])
    Headers += 'X-Ca-Stage:{}\n'.format(headers['X-Ca-Stage'])
    Headers += 'X-Ca-Timestamp:{}\n'.format(headers['X-Ca-Timestamp'])
    query = '&'.join([f'{k}={params[k]}' for k in sorted(params)])
    query += '&'.join([f'{k}={data[k]}' for k in sorted(data)])
    url_query = f'{path}?{query}' if query else path

    # 被签名原数据
    sign = HTTPMethod + '\n' + Accept + '\n' + Content_MD5 + '\n' + Content_Type + '\n' + Date + '\n' + Headers + url_query
    # 进行签名
    signature_hmac = hmac.new(secret.encode('utf-8'), sign.encode('utf-8'), 'sha256')
    signature = base64.b64encode(signature_hmac.digest())
    # 把签名放进headers
    headers['X-Ca-Signature'] = signature.decode('utf8')
    # 屏蔽https证书警告
    urllib3.disable_warnings()
    # 发送请求
    response = requests.request(method=method, url=f"{channel}://{host}{path}", headers=headers, params=params,
                                data=data, json=data_json, verify=False)
    return response


if __name__ == '__main__':
    # def code():
    #     r = request(path='/api/account/sendCode?mobile=16639051485', method='get')
    #     return r.json()
    #
    #
    # print(code())
    def code():
        r = request(path='/api/basic/sendcode?mobile=16639051485', method='get')
        return r.json()


    # print(code())
    # 登录接口

    r = request(path='/api/basic/signin', method='post', data_json={
        "mobile": "16639051485",
        "code": "1234"
    })
    print(r.json())
    # token_data = r.json()['data']['token']
