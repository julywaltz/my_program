#!/usr/bin/env python
# -*- coding=utf-8 -*-

# @Author: Cheng Yili
# @Date: 2019-09-10 22:31:58
# @LastEditors: Cheng Yili
# @LastEditTime: 2019-09-10 22:31:58
# @Email: julywaltz77@hotmail.com

from selenium import webdriver
import time
import yaml
import os
from random import randint, choice
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
    for i in cookieBefore:
        print(i)
    # 加一个休眠，这样得到的cookie 才是登录后的cookie,否则可能打印的还是登录前的cookie
    print('请扫码')
    time.sleep(10)
    # 获取登陆后的cookies
    print("登陆成功")
    getCookies(driver)
    print('关闭浏览器')
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
        time.sleep(1)
    # 这里重新获取地址再次指定网址。
    # 刷新查看登录状态
    driver.refresh()
    time.sleep(5)
    # 重新获取cookies 并写入config.yaml文件
    getCookies(driver)


"""自动开始学习保证15分"""


def startLearn():
    print('自动登录中，请稍等！')
    url = 'https://pc.xuexi.cn/points/my-points.html'
    driver = webdriver.Firefox()
    login(url, driver)
    time.sleep(randint(2, 3))
    print('跳转中')
    driver.find_element_by_link_text("学习强国").click()
    print('跳转完成')
    time.sleep(randint(2, 4))
    allhandles = driver.window_handles
    print("跳转中")
    driver.switch_to.window(allhandles[-1])
    driver.implicitly_wait(randint(3, 5))
    driver.find_element_by_xpath(".//span[contains(text(),'学习时评')]").click()
    time.sleep(randint(2, 3))
    allhandles = driver.window_handles
    driver.switch_to.window(allhandles[-1])
    print("跳转完成", allhandles, allhandles[-1])
    for i in range(1, 7):
        time.sleep(randint(2, 4))
        print("跳转中", allhandles)
        driver.find_element_by_xpath(
            '//div[@class="grid-cell"][{}]/div/div[@class="text-link-item-title"]/div[@class="text-wrap"]/span[@class="text"]'
            .format(i)).click()
        time.sleep(randint(2, 3))
        allhandles = driver.window_handles
        driver.switch_to.window(allhandles[-1])
        print("跳转完成", allhandles, allhandles[-1])
        print("阅读中")
        time.sleep(randint(30, 40))
        driver.execute_script("document.documentElement.scrollTop=1000")
        time.sleep(randint(20, 40))
        driver.execute_script("document.documentElement.scrollTop=2000")
        time.sleep(randint(10, 20))
        print('阅读完毕')
        driver.close()
        allhandles = driver.window_handles
        driver.switch_to.window(allhandles[-1])
        print('关闭页面', allhandles, allhandles[-1])
    print("跳转中")
    driver.close()
    allhandles = driver.window_handles
    driver.switch_to.window(allhandles[-1])
    driver.find_element_by_link_text("学习电视台").click()
    allhandles = driver.window_handles
    driver.switch_to.window(allhandles[-1])
    time.sleep(randint(2, 3))
    print('跳转完成', allhandles, allhandles[-1])
    xxdst_list = [
        '第一频道', '理论频道', '党史频道', '人物频道', '文艺频道', '科学频道', '自然频道', '法治频道', '军事频道',
        '理论频道', '党史频道', '教育频道'
    ]
    driver.find_element_by_xpath(".//span[contains(text(),'{}')]".format(
        choice(xxdst_list))).click()
    print("跳转中")
    time.sleep(randint(2, 3))
    allhandles = driver.window_handles
    driver.switch_to.window(allhandles[-1])
    print('跳转完成', allhandles, allhandles[-1])
    for j in range(1, 6):
        time.sleep(randint(3, 4))
        driver.find_element_by_xpath(
            '//div[@class="grid-gr"][{}]/div/section/div/div/div/div/div/div/div/div'
            .format(j)).click()
        allhandles = driver.window_handles
        driver.switch_to.window(allhandles[-1])
        time.sleep(randint(2, 3))
        video = driver.find_element_by_xpath(
            '//div[@class="outter"]').click()  # 找到视频
        time.sleep(randint(180, 240))
        driver.close()
        allhandles = driver.window_handles
        driver.switch_to.window(allhandles[-1])
        print('关闭页面', allhandles, allhandles[-1])


if __name__ == "__main__":
    if 'config.yaml' not in os.listdir(os.getcwd()):
        print(os.listdir(os.getcwd()))
        """ theFirstTimeLogin()
    else:
      startLearn() """
