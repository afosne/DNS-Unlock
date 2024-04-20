#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@Author: DC3x6
@Created: 2020-4-10 
"""

import json,base64,xlwt
import requests as req
import configparser



def get_data():
    try:
        for url,s in zip(url_list, q_list):
            # print(url)
            # resp = req.get(url=url, headers=headers, proxies=proxies, timeout=30)
            resp = req.get(url=url, headers=headers, timeout=30)
            en_json = json.loads(resp.content, encoding=('utf8'))
            save_data(en_json,s)
    except Exception as e:
        print (e)




def save_data(en_json,s):
    lenth = len(fields_list)
    book = xlwt.Workbook(encoding='utf-8', style_compression=0)
    sheet = book.add_sheet('sheet', cell_overwrite_ok=True)
    sheet.write(0, 0, '序号')
    for i in range(0, lenth):
        sheet.write(0, i + 1, fields_list[i])
    sheet.write(0, lenth + 1, '模式')
    sheet.write(0, lenth + 2, 'error')
    sheet.write(0, lenth + 3, '语法')
    sheet.write(0, lenth + 4, '页数')
    sheet.write(0, lenth + 5, '大小')
    sheet.write(0, lenth + 6, 'url')
    r = 1
    for i in en_json['results']:
        sheet.write(r, 0, r)
        for k in range(0, lenth):
            sheet.write(r, k + 1, i[k])
        sheet.write(r, lenth + 1, en_json['mode'])
        sheet.write(r, lenth + 2, en_json['error'])
        sheet.write(r, lenth + 3, en_json['query'])
        sheet.write(r, lenth + 4, en_json['page'])
        sheet.write(r, lenth + 5, en_json['size'])
        if 'https' in i[0] :
            sheet.write(r, lenth + 6, i[0])
        elif 'https' in i[4] and 'https://' not in i[0]:
            sheet.write(r, lenth + 6, 'https://'+i[0])
        elif 'http' not in i[4] :
            sheet.write(r, lenth + 6, 'http://'+i[0])
        elif 'http://' not in i[0] and 'http' in i[4] :
            sheet.write(r, lenth + 6, 'http://' + i[0])
        else:
            pass
        r = r + 1
    book.save('%s.xls'%s)
    # cwd = os.getcwd()
    # dir = cwd + '\\' + 'targets.txt'
    # k = len(en_json['results'])
    # try:
    #     with io.open(dir, 'w', encoding='utf-8') as f:
    #         for i in range(0, k):
    #             s = en_json['results'][i]
    #             f.write(s+'\n')
    # except Exception as e:
    #     print e


if __name__ == '__main__':
    config = configparser.ConfigParser()
    config.read('info.ini', encoding='utf-8')
    email = config['REQUESTS']['email']
    key = config['REQUESTS']['key']
    size = config['REQUESTS']['size']
    page = config['REQUESTS']['page']
    full = config['REQUESTS']['full']
    fields = config['REQUESTS']['fields']
    fields_list = fields.split(',')
    url_list = []
    q_list = []
    for i in config['KEYWORDS']:
        q_list.append(i)
        q = (base64.b64encode(config['KEYWORDS'][i].encode('utf-8')).decode('utf-8'))
        url_list.append('https://fofa.so/api/v1/search/all?email=' + email + '&key=' + key + "&qbase64=" + q + '&size=' + size + '&page' + page + '&fields=' + fields + '&full=' + full)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:68.0) Gecko/20100101 Firefox/68.0',
        'Accept': '*/*'
    }
    proxies = {
        "http": "127.0.0.1:12315",
        "https": "127.0.0.1:12315"
    }
    if url_list:
        get_data()
    else:
        print ("请检查配置文件")

