#!/usr/bin/python
# -*- coding: UTF-8 -*-

from selenium import webdriver  # 导入webdriver模块
import re   # 导入正则模块

driver = webdriver.Chrome() # Google Chrome浏览器
driver.get('http://sck.rjkflm.com:666/spider/jigsaw/') # 启动网页
swiper = driver.find_element_by_xpath('/html/body/div/div[2]/div[2]/span[1]') # 获取按钮滑块
action = webdriver.ActionChains(driver) # 创建动作
action.click_and_hold(swiper).perform() # 单击并保证不松开
action.move_by_offset(0,0).perform()    # 滑动0距离，不松手，不执行该动作无法获取图形滑块left值
verify_style = driver.find_element_by_xpath('/html/body/div/div[2]/div[1]/div[1]').get_attribute('style')   # 获取图形模块样式
verified_style = driver.find_element_by_xpath('/html/body/div/div[2]/div[1]/div[2]').get_attribute('style') # 获取空缺滑块样式
verified_left = float(re.findall('left:(.*?)px;',verified_style[0])) # 获取空缺滑块left值
verify_left = float(re.findall('left:(.*?)px;',verify_style[0]))    # 获取图形滑块left值
action.move_by_offset(verified_left-verify_left,0)  # 滑动指定距离
action.release().perform()  # 松开鼠标
