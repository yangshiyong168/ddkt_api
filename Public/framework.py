#coding=utf-8

import requests,xlrd,xlwt,time,hashlib
from xlutils.copy import copy
from ddkt_api.Config.Api_Data import *
def apiRequests(type, url, data, head):
    """get和post请求一起处理函数"""
    if type =='get':
        res = requests.get(url,data,headers=head,timeout=10)
    else:
        res = requests.post(url,data,headers=head,timeout=10)
    print(res.json())
    return res

def readExcel(filename, sheetname, line):
    """读取excel指定行的数据"""
    book=xlrd.open_workbook(filename)
    sheet=book.sheet_by_name(sheetname)
    data=sheet.row_values(int(line))
    return data

def writExcel(filename, sheetname, line, row, data):
    """写入文件指定的单元格内容,不会清楚其它单元格的数据"""
    file=xlrd.open_workbook(filename,formatting_info=True)  # 打开文件
    wb=copy(file)  # 利用xlutils.copy下的copy函数复制
    ws=wb.get_sheet(sheetname)   # 指定表格的sheet页面
    ws.write(line,row,data)   # 写入数据
    wb.save(filename)  # 保存文件

def fixExcel(filename, sheetname, line, row, data_1, data_2):
    """修改文件指定的单元格内容"""
    data=readExcel(filename, sheetname, line)
    if '&' in data[5]:
        list=data[5].split('&')
    else:
        list=[data[5]]
    value=""
    for i in list:  ##循环读取列表修改其中的值
        if data_1 in i:
            list[list.index(i)]=data_2
    for j in list:  ##循环读取列表进行拼接
        value=value+j+'&'
    value=value.strip('&')
    writExcel(filename, sheetname, line, row, value) ##调用写入表格函数，不清除其它数据
    # file=xlrd.open_workbook(filename, formatting_info=True)   # 打开文件回写
    # wb=copy(file)  # 利用xlutils.copy下的copy函数复制
    # ws=wb.get_sheet(sheetname)   # 指定表格的sheet页面
    # ws.write(line, row, value)   # 写入数据
    # wb.save(filename)  # 保存文件


def encryption(filename, sheetname, line):
    """读取传输的参数，并转成字典格式，进行加密处理"""
    data=readExcel(filename, sheetname, line)
    dict={}
    time1=getTimestamp() ##获取当前时间戳
    dict['dd_timestamp']=time1 ##将时间搓加入到参数里面
    if '&' in data[5]:
        list=data[5].split('&')
        for i in list:
            dict[i.split('=')[0]] = i.split('=')[1]
    elif '=' in data[5]:
        dict[data[5].split('=')[0]] = data[5].split('=')[1]
    else:
        pass
    sign=getSign(filename, sheetname, line, time1)
    dict['dd_sign'] = sign
    return dict

def getSign(filename, sheetname, line, time1):
    """从excel里获取参数，处理后输出sign参数"""
    data = readExcel(filename, sheetname, line)
    value=ddversion
    if '&' in data[5]:  ##参数大于等于一个时
        data1=data[5].split('&')
        data1.append('dd_timestamp='+str(time1))
        data1.sort()
        for i in data1:
            value=value+str(i).strip()
    elif  '=' in data[5]:  ##参数只有一个的情况
        data1=[data[5]]
        data1.append('dd_timestamp=' + str(time1))
        data1.sort()
        for i in data1:
            value=value+str(i).strip()
    else:         ##参数为空的情况
        value=value+'dd_timestamp=' + str(time1)
    # value=value+"yunkey=90DLUCK07PHP-APPLE0EF5-G4DD-ANDROIDEB9F"
    value = value + "yunkey=AD6C7B7AF608ADE16A31C729193E038A"
    sign=MD5_Encryption(value).upper()  ##转换成MD5后转大写
    return sign

def getTimestamp():
    """获取当前时间戳"""
    time1=int(time.time())
    return time1

def MD5_Encryption(text):
    """进行MD5加密"""
    m = hashlib.md5()
    m.update(text.encode(encoding='utf-8'))
    sign=m.hexdigest()
    return sign

def Get_verify_code(data):
    """获取验证码"""
    list = data[5].split("&")
    phonenum = "13530655679"
    for i in list:
        if "mobile" in i:
            phonenum = i.split("=")[1]
    return data[0][0]

if __name__ == '__main__':

    name='C:\\automation\\DdktAPI\\Testdata\\data.xls'







