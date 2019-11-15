#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#  __author__ = "ffadmin"
"""
ex:
  将fandaguai文件夹下的所有以xls结尾的表格读取生成到当前目录下的新表格
  并去重
  $python excel_handle.py fandaguai
"""

import xlrd,xlwt,os,datetime,sys


def read_xls(excel_directory):
    #获取文件夹下的xls文件
    __excel_data = []
    list = os.listdir(excel_directory)
    for i in list:
        if os.path.splitext(i)[1] == '.xls':
            #print(i)
            file_xls = xlrd.open_workbook("%s/%s"%(excel_directory,i))
            #获取第0个索引的sheet
            sheet_index = file_xls.sheet_by_index(0)
            num_rows = sheet_index.nrows
            #print(num_rows)
            #获取说有表格内容，添加到list
            for i in range(1,num_rows):
                test = sheet_index.row_values(i)
                __excel_data.append(test)
    __new_excel_data = []
    for cont in __excel_data:
        if cont not in __new_excel_data:
            __new_excel_data.append(cont)
    return (__new_excel_data)


def write_xls(excel_directory):
    __book = xlwt.Workbook()  # 创建一个Excel
    __sheet1 = __book.add_sheet('data')  # 在其中创建一个名为data的sheet
    __data = read_xls(excel_directory)
    __l12 = list(range(len(__data)))
    __dict1 = dict(zip(__l12,__data))
    #print(dict1)
    ldata = []
    num = [a for a in __dict1]
    # for循环指定取出key值存入num中
    num.sort()
    # 字典数据取出后无需，需要先排序
    for x in num:
        # for循环将data字典中的键和值分批的保存在ldata中
        t = [int(x)]
        for a in __dict1[x]:
            t.append(a)
        ldata.append(t)
    for i, p in enumerate(ldata):
        # 将数据写入文件,i是enumerate()函数返回的序号数
        for j, q in enumerate(p):
            #print(i,j,q)
            __sheet1.write(i, j, q)
    __book.save("demo.xls")


if __name__ == '__main__':
    start_time = datetime.datetime.now()
    #print(start_time)
    write_xls(sys.argv[1])
    end_time = datetime.datetime.now()
    total_time = end_time - start_time
    #print(end_time)
    print("用时：%s"%total_time)
    print("===================end=====================")
