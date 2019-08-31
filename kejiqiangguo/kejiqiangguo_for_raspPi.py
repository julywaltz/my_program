#!/usr/bin/env python
# -*- coding=utf-8 -*-

# @Author: Cheng Yili
# @Date: 2019-07-16 22:23:08
# @LastEditors: Cheng Yili
# @LastEditTime: 2019-08-31 22:45:14
# @Email: julywaltz77@hotmail.com

# -*- coding: utf-8 -*-
# @Author: Cheng Yili
# @Date:   2019-07-15 20:16:12
# @Email:  julywaltz77@hotmail.com
# @Last Modified by:   Cheng Yili
# @Last Modified time: 2019-07-15 22:01:09

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import os
from random import randint, choice, sample
import time


"""自动开始学习保证15分"""


def startLearn(driver, url):
    driver.get(url)
    driver.maximize_window()
    time.sleep(2)
    driver.execute_script("document.documentElement.scrollTop=2000")
    print('请扫码')
    time.sleep(15)
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
        allhandles = driver.window_handles
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
        c = choice(xxdst_list)
        print('打开{}'.format(c))
        driver.find_element_by_xpath(".//span[contains(text(),'{}')]".format(
            c)).click()  #随机选取上述列表中的频道进行观看
        print("跳转中")
        time.sleep(randint(2, 3))
        allhandles = driver.window_handles
        driver.switch_to.window(allhandles[-1])
        print(allhandles, allhandles[-1])
        print('跳转完成')
        try:
            for i in sample(range(1, 4), 2):
                time.sleep(randint(5, 7))
                for j in sample(range(1, 5), 3):
                    driver.find_element_by_xpath(
                        '//div[@class="grid-gr"][{}]/div[{}]/section/div/div/div/div/div/div/div/div'
                        .format(i)).click()
                    allhandles = driver.window_handles
                    driver.switch_to.window(allhandles[-1])
                    time.sleep(randint(3, 6))
                    driver.find_element_by_xpath(
                        '//div[@class="outter"]').click()
                    time.sleep(randint(300, 600))
                    driver.close()
                    print('关闭页面')
                    allhandles = driver.window_handles
                    driver.switch_to.window(allhandles[-1])
        except:
            for i in sample(range(1, 3), 1):
                time.sleep(randint(5, 7))
                for j in range(1, 5):
                    print('开始播放视频')
                    driver.find_element_by_xpath(
                        '//div[@class="grid-gr"][{}]/div[{}]/section/div/div/div/div/div/div/div/div'
                        .format(i, j)).click()
                    allhandles = driver.window_handles
                    driver.switch_to.window(allhandles[-1])
                    time.sleep(randint(3, 6))
                    driver.find_element_by_xpath(
                        '//div[@class="outter"]').click()
                    time.sleep(randint(300, 600))
                    driver.close()
                    print('关闭页面')
                    allhandles = driver.window_handles
                    driver.switch_to.window(allhandles[-1])
    else:
        pass
    driver.quit()


if __name__ == "__main__":
    print('欢迎食用~')
    url = 'https://pc.xuexi.cn/points/my-points.html'
    chrome_options = Options()
    driver = webdriver.Chrome(chrome_options=chrome_options,
                              executable_path="/usr/bin/chromedriver")
    try:
        startLearn(driver, url)
    except:
        print('程序出错，自动重启中')
        try:
            startLearn(driver, url)
        except:
            print('程序出错，自动重启中')
            try:
                startLearn(driver, url)
            except:
                print('程序出错，自动重启中')
                try:
                    startLearn(driver, url)
                except:
                    print('程序出错，自动重启中')
                    startLearn(driver, url)
    finally:
        print('程序关闭！')
