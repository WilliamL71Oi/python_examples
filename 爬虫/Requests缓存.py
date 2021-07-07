#!/usr/bin/env python
# -*- coding=utf-8 -*-
# 通过配置钩子函数可以实现：在第一次请求时，因为没有请求缓存所以执行了2秒等待延迟时；当第二次请求时则没有执行2秒延时，并输出是否存在请求缓存为True。
# 在发送网络请求爬取网页数据时，如果频繁地发送网络请求，后台服务器则会视为爬虫程序，此时将会采取反爬措施，所以多次请求中要出现一定的间隔时间，设置延时是一个不错的选择。
# 但是如果在第一次请求后已经生成了缓存，那么第二次请求也就无需设置延时，对于此类情况Requests-Cache模块可以使用自定义钩子函数的方式，合理地判断是否需要设置延时操作
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
