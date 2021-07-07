#!/usr/bin/env python
# -*- coding=utf-8 -*-

import requests_cache
import time

requests_cache.install_cache()  # 设置缓存
requests_cache.clear()  # 清理缓存

# 定义钩子  
def make_throttle_hook(timeout=0.1):
    def hook(response, *args, **kwargs):
        print(response.text)  # 打印请求结果
        if not getattr(response, 'from_cache', False):
            print('等待', timeout, '秒！')
            time.sleep(timeout) # 等待指定时间
        else:
            print(response.from_cache)  # 存在缓存输出True
        return response

    return hook


if __name__ == '__main__':
    requests_cache.install_cache()  # 创建缓存
    requests_cache.clear()  # 清理缓存
    s = requests_cache.CachedSession()  # 创建缓存会话
    s.hooks = {'response': make_throttle_hook(2)} # 配置钩子函数
    s.get('http://httpbin.org/get') # 模拟发送第一次网络请求
    s.get('http://httpbin.org/get') # 模拟发送第二次网络请求
