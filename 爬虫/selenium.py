#! /usr/bin/python3
# -*- coding: UTF-8 -*-

from selenium import webdriver  # 导入浏览器驱动模块
from selenium.webdriver.support.wait import WebDriverWait  # 导入等待类
from selenium.webdriver.support import expected_conditions as EC  # 等待条件
from selenium.webdriver.common.by import By  # 节点定位

try:
    # 创建谷歌浏览器驱动参数对象
    chrome_options = webdriver.ChromeOptions()
    # 不加载图片
    prefs = {"profile.managed_default_content_settings.images": 2}
    chrome_options.add_experimental_option("prefs", prefs)
    # 使用headless无界面浏览器模式
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    # 加载谷歌浏览器驱动
    driver = webdriver.Chrome(options=chrome_options, executable_path=r"D:\唯品会\python\爬虫\chromedriver.exe")
    # 请求地址
    driver.get("https://item.jd.com/12353915.html")
    wait = WebDriverWait(driver, 10)
    # 等待页面加载class名称m-item-inner的节点，该节点中包含商品信息
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, "m-item-inner")))
    # 获取name节点中的所有div节点
    name_div = driver.find_element_by_css_selector('#name').find_element_by_tag_name('div')
    summary_price = driver.find_element_by_id('summary-price')
    print("获取的商品标题如下：")
    print(name_div[0].text)
    print("提取的商品宣传语如下：")
    print(name_div[1].text)
    print("提取的编著信息如下：")
    print(name_div[4].text)
    print("商品价格信息如下：")
    print(summary_price.text)
    driver.quit()
except Exception as e:
    print("显示异常信息！", e)
