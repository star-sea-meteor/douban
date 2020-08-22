# -*- coding: utf-8 -*-
"""
==================================================================================================
                            File Name   : douban_book.py
                            Author      : 杨卓尧
                            Date        : 2020-8-22
                            Change Date : 2020-8-22
==================================================================================================
"""
# 导入模块
import html

import requests
from lxml import etree

# 声明请求头文件
headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36"}
# requests爬取top250 内容
all_html = ""
for i in range(10):
    spider_url = "https://book.douban.com/top250?start=%d" % (i * 25)
    html = requests.get(url=spider_url, headers=headers)
    html.encoding = "utf-8"
    all_html += html.text
# 生成lxml对象
lxml = etree.HTML(all_html)
# 使用xpath提取,格式化输出信息
tables = lxml.xpath("//*[@id='content']/div/div[1]/div/table")
for table in tables:
    name = table.xpath("./tr/td[2]/div[1]/a/text()")[0].strip()
    score = table.xpath("./tr/td[2]/div/span[2]/text()")[0].strip()
    evaluation_num = table.xpath(
        './tr/td[2]/div/span[3]/text()')[0].replace('(', '').replace(')', '').strip()
    message = table.xpath("./tr/td[2]/p[1]/text()")[0].strip()
    quotation = table.xpath(
        "./tr/td[2]/p[2]/span/text()")
    print("《{}》  {} 分  {}  {} \n{}".format(
        name, score, evaluation_num, message, quotation))