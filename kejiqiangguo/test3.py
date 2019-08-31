#!/usr/bin/env python
# -*- coding=utf-8 -*-

# @Author: Cheng Yili
# @Date: 2019-08-31 22:03:39
# @LastEditors: Cheng Yili
# @LastEditTime: 2019-08-31 22:09:13
# @Email: julywaltz77@hotmail.com

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

import time
import yaml
import os
from random import randint, choice, sample
import time
"""首次登陆需要根据提示扫码"""
"""自动开始学习保证15分"""


def startLearn():
    chrome_options = Options()
    url = 'https://pc.xuexi.cn/points/my-points.html'
    driver = webdriver.Chrome()
    driver.get(url)
    driver.maximize_window()
    driver.execute_script("document.documentElement.scrollTop=2000")
    time.sleep(2)
    print('请扫码')
    time.sleep(20)
    # 获取登陆后的cookies
    print("登陆成功")
    time.sleep(randint(2, 3))
    print('跳转中')
    if driver.find_element_by_xpath(
            '//div[@class="my-points-card"][2]/div[2]/div[2]/div'
    ).get_attribute('textContent') == '去看看':
        driver.find_element_by_link_text("学习强国").click()
        print('跳转完成')
        time.sleep(randint(2, 4))
        allhandles = driver.window_handles
        print("跳转中")
        driver.switch_to.window(allhandles[-1])
        driver.implicitly_wait(randint(5, 6))
        driver.find_element_by_xpath(
            ".//span[contains(text(),'学习时评')]").click()
        time.sleep(randint(2, 3))
        allhandles = driver.window_handles
        driver.switch_to.window(allhandles[-1])
        print(allhandles, allhandles[-1])
        print("跳转完成")
        for i in sample(range(1, 13), 6):  # 随机选取六篇文章观看
            time.sleep(randint(5, 7))
            print("跳转中", allhandles)
            driver.find_element_by_xpath(
                '//div[@class="grid-cell"][{}]/div/div[@class="text-link-item-title"]/div[@class="text-wrap"]/span[@class="text"]'
                .format(i)).click()
            time.sleep(randint(2, 3))
            allhandles = driver.window_handles
            driver.switch_to.window(allhandles[-1])
            print("跳转完成", allhandles, allhandles[-1])
            print("阅读中")
            time.sleep(randint(40, 60))
            driver.execute_script("document.documentElement.scrollTop=1000")
            time.sleep(randint(60, 75))
            driver.execute_script("document.documentElement.scrollTop=2000")
            time.sleep(randint(40, 65))
            print('阅读完毕')
            driver.close()
            allhandles = driver.window_handles
            driver.switch_to.window(allhandles[-1])
            print('关闭页面')
            print(allhandles, allhandles[-1])
        allhandles = driver.window_handles
        driver.switch_to.window(allhandles[-1])
        driver.close()
        allhandles = driver.window_handles
        driver.switch_to.window(allhandles[-1])
        driver.close()
        driver.switch_to.window(allhandles[-1])
    else:
        pass
    allhandles = driver.window_handles
    print(allhandles, allhandles[-1])
    print("跳转中")
    time.sleep(randint(1, 2))
    if driver.find_element_by_xpath(
            '//div[@class="my-points-card"][3]/div[2]/div[2]/div'
    ).get_attribute('textContent') == '去看看':
        driver.find_element_by_link_text("学习强国").click()
        print('跳转完成')
        time.sleep(randint(2, 4))
        allhandles = driver.window_handles
        driver.switch_to.window(allhandles[-1])
        driver.find_element_by_link_text("学习电视台").click()
        allhandles = driver.window_handles
        driver.switch_to.window(allhandles[-1])
        time.sleep(randint(5, 6))
        print(allhandles, allhandles[-1])
        print('跳转完成')
        xxdst_list = [
            '第一频道', '理论频道', '党史频道', '人物频道', '文艺频道', '科学频道', '自然频道', '法治频道',
            '军事频道', '理论频道', '党史频道', '教育频道'
        ]
        driver.find_element_by_xpath(".//span[contains(text(),'{}')]".format(
            choice(xxdst_list))).click()  #随机选取上述列表中的频道进行观看
        print("跳转中")
        time.sleep(randint(2, 3))
        allhandles = driver.window_handles
        driver.switch_to.window(allhandles[-1])
        print(allhandles, allhandles[-1])
        print('跳转完成')
        for i in sample(range(1, 13), 5):
            time.sleep(randint(5, 7))
            driver.find_element_by_xpath(
                '//div[@class="grid-gr"][{}]/div/section/div/div/div/div/div/div/div/div'
                .format(j)).click()
            allhandles = driver.window_handles
            driver.switch_to.window(allhandles[-1])
            time.sleep(randint(3, 6))
            video = driver.find_element_by_xpath(
                '//div[@class="outter"]').click()  # 找到视频
            time.sleep(randint(300, 600))
            driver.close()
            allhandles = driver.window_handles
            driver.switch_to.window(allhandles[-1])
            print('关闭页面', allhandles, allhandles[-1])
    else:
        pass


if __name__ == "__main__":
    print('欢迎食用~')
    try:
        startLearn()
    except:
        print('程序错误，自动重启中，请稍侯！')
        time.sleep(10)
        startLearn()
    finally:
        driver.quit()
