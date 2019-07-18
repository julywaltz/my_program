#!/usr/bin/env python
# -*- coding=utf-8 -*-

# @Author: Cheng Yili
# @Date: 2019-07-16 22:23:08
# @LastEditors: Cheng Yili
# @LastEditTime: 2019-07-18 20:54:26
# @Email: julywaltz77@hotmail.com

# -*- coding: utf-8 -*-
# @Author: Cheng Yili
# @Date:   2019-07-15 20:16:12
# @Email:  julywaltz77@hotmail.com
# @Last Modified by:   Cheng Yili
# @Last Modified time: 2019-07-15 22:01:09

from selenium import webdriver
import time
import yaml
import os
from random import randint, choice, sample
from selenium import webdriver
import time
"""首次登陆需要根据提示扫码从而获取cookies并保存在本地"""


def theFirstTimeLogin():
    url = 'https://pc.xuexi.cn/points/my-points.html'
    driver = webdriver.Firefox()
    driver.get(url)
    driver.maximize_window()
    time.sleep(2)
    print('请等待，获取自动登陆的cookies')
    cookieBefore = driver.get_cookies()
    # 打印登录前的cookie
    # 加一个休眠，这样得到的cookie 才是登录后的cookie,否则可能打印的还是登录前的cookie
    print('请扫码')
    time.sleep(20)
    # 获取登陆后的cookies
    print("登陆成功")
    getCookies(driver)
    driver.quit()


"""获取cookis并写入config.yaml文件"""


def getCookies(driver):
    print('获取cookies')
    cookiesNew = driver.get_cookies()
    print('获取结束')
    print('开始写入')
    # 获取当前文件所在路径
    fileNamePath = os.path.split(os.path.realpath(__file__))[0]
    # 拼接config.yaml文件绝对路径
    yamlPath = os.path.join(fileNamePath, 'config.yaml')
    fw = open(yamlPath, 'w', encoding='utf-8')
    # 构建数据
    yaml.dump(cookiesNew, fw)
    print('写入结束')


def cookies_set():
    f = open('config.yaml', 'r', encoding='utf8')
    y = yaml.load(f)
    print(y, type(y))
    f.close()
    cookieNew = []
    for i in y:
        if 'expiry' in i:
            i['expiry'] = i['expiry'] * 24
        cookieNew.append(i)
    f = open('config.yaml', 'w', encoding='utf8')
    yaml.dump(cookieNew, f)
    f.close()


"""自动登陆后重新获取cookie并覆盖写入config.ymal文件"""


def login(url, driver):
    driver.maximize_window()
    # 清除一下cookie
    driver.delete_all_cookies()
    time.sleep(3)
    driver.get(url)
    fileNamePath = os.path.split(os.path.realpath(__file__))[0]
    yamlPath = os.path.join(fileNamePath, 'config.yaml')
    # 读取yaml 文件
    f = open(yamlPath, 'r', encoding='utf-8')
    cont = f.read()
    cookies = yaml.load(cont)
    # 读取cookie值
    for cookie in cookies:
        driver.add_cookie(cookie)
        time.sleep(2)
    # 刷新查看登录状态
    driver.refresh()
    time.sleep(5)


"""自动开始学习保证15分"""


def startLearn(driver, url):
    print('自动登录中，请稍等！')
    login(url, driver)
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
    getCookies(driver)
    cookies_set()


if __name__ == "__main__":
    print('欢迎食用~')
    if 'config.yaml' not in os.listdir(os.getcwd()):
        print(os.getcwd())
        theFirstTimeLogin()
    url = 'https://pc.xuexi.cn/points/my-points.html'
    driver = webdriver.Firefox()
    try:
        startLearn(driver, url)
    except:
        print('程序错误，自动重启中，请稍侯！')
        time.sleep(10)
        startLearn(driver, url)
    finally:
        driver.quit()
