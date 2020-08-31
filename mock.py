#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 19 23:41:40 2020
@author: kath
"""
import pandas as pd
import datetime
import configparser
from FunctionClassConfig import findFunction,findClass
from sqlalchemy import create_engine
from FakerData import *
from faker import Faker

def mockdata():
    start = datetime.datetime.now()
    # 解决configparser不区分大小写的问题
    class MyConfigParser(configparser.RawConfigParser):
        def __init__(self, defaults=None):
            configparser.RawConfigParser.__init__(self, defaults=defaults)
        def optionxform(self, optionstr):
            return optionstr
    #连接数据库
    conf = MyConfigParser()
    conf.read('config_all.conf',encoding='utf-8')
    conn = conf.get('sql_config','数据库类型') + '+' + conf.get('sql_config','数据库驱动选择') + '://' + conf.get('sql_config','用户名') + ':' + conf.get('sql_config','密码') + '@' + conf.get('sql_config','服务器') + ':' + conf.get('sql_config','端口') + '/' + conf.get('sql_config','目标数据库名')
    db_name = conf.get('sql_config','目标数据库名')
    print(conn)
    try:
        connection = create_engine(conn)
    except:
        print('ERROR:cannot connect mysql database.')
    #循环表个数
    tb_cnt = conf.sections()
    for i in tb_cnt:
        if not i.startswith('t'):
            tb_cnt.remove(i)
    tb_cnt = len(tb_cnt)
    #读type，判断是否有关联表
    tp_list = []
    for i in range(1,tb_cnt+1):
         tp_list.append(conf.get('table_{}'.format(i), "type"))
         locals()['list_{}'.format(i)] = ['table_{}'.format(i),conf.get('table_{}'.format(i), "type")]
    tp_list1 = set(tp_list)
    for i in tp_list1:
        tb_conf = []
        #无关联表的生成：
        if tp_list.count(i) == 1:
            print('start irre:')
            #找到相应的section名称
            for j in range(1,tb_cnt+1):
                if i in locals()['list_{}'.format(j)]:
                    sec = locals()['list_{}'.format(j)][0]
            #读取表名
            tb_name = conf.get(sec,'tb_name')
            #读取字段到list
            cols = conf.get(sec,'columns')
            cols = cols.split(',')
            #读取行数
            row_number = int(conf.get(sec,'row_number'))       #格式str
            #开始随机数，构造dataframe
            df = pd.DataFrame(columns=cols)       #创建df表头
            create_time = datetime.datetime.strftime(datetime.datetime.now(),'%Y-%m-%d')       #生成当前日期
            values = ''
            for j in range(0,row_number):
                for i in cols:
                    c = findClass(findFunction(i))      #读fakerdata的类和函数
                    f = eval(c + '.' + findFunction(i)+'()')   #读fakerdata的函数
                    #构造dataframe主体内容，避免分隔符重复，dataframe中的分隔符使用"|"
                    values = values + "'" + str(f) + "'" + '|'
                values = values.rstrip('|')
                values = values.replace("\'", "")
                df.loc[len(df)] = values.split('|')
                values = ''
            #将dataframe写入csv
            df.to_csv('mockdata_'+tb_name+'_'+create_time+'.csv',index = False,encoding = 'gbk')
            #写入数据库
            try:
                # pd.io.sql.to_sql(df,tb_name,con=connection,schema=db_name,if_exists='replace',index = False,index_label = False)
                pd.io.sql.to_sql(df,tb_name,con=connection,schema=db_name,if_exists='replace',index = True,index_label = "Id")
            except:
                print('ERROR:cannot insert into mysql.')
            print('----table "'+tb_name+'" finished----')
        #有关联表的生成
        else:
            print('start rel:')
            secs = []
            for j in range(1,tb_cnt+1):
                if i in locals()['list_{}'.format(j)]:
                    #找到相应的section名称
                    secs.append(locals()['list_{}'.format(j)][0])
            #设置总表表名
            tb_name = 'general table type '+i
            #获取生成总表所需的信息
            #读取所有字段到list
            cols = []
            for k in secs:
                each_col = conf.get(k,'columns').split(',')
                for n in each_col:
                    if not n in cols:
                        cols.append(n)
            #读最大行数
            row_number = int(conf.get(secs[0],'row_number'))
            for k in secs:
                if int(conf.get(k,'row_number')) > int(conf.get(secs[0],'row_number')):
                    row_number = int(conf.get(k,'row_number'))
            #开始随机数，构造dataframe
            df = pd.DataFrame(columns=cols)       #创建df表头
            create_time = datetime.datetime.strftime(datetime.datetime.now(),'%Y-%m-%d')       #生成当前日期
            values = ''
            for j in range(0,row_number):
                for i in cols:
                    c = findClass(findFunction(i))      #读fakerdata的类和函数
                    f = eval(c + '.' + findFunction(i)+'()')   #读fakerdata的函数
                    #构造dataframe主体内容，避免分隔符重复，dataframe中的分隔符使用"|"
                    values = values + "'" + str(f) + "'" + '|'
                values = values.rstrip('|')
                values = values.replace("\'", "")
                df.loc[len(df)] = values.split('|')
                values = ''
            #将dataframe写入csv
            df.to_csv('mockdata_'+tb_name+'_'+create_time+'.csv',index = False,encoding = 'gbk')
            
            for k in secs:
                tb_name1 = conf.get(k,'tb_name')
                cols1 = conf.get(k,'columns').split(',')
                row_number1 = int(conf.get(k,'row_number'))

                #构造各子表
                df1 = df[:row_number1][cols1]
                #print(df1)
                df1.to_csv('mockdata_'+tb_name1+'_'+create_time+'.csv',index = False,encoding = 'gbk')
                #dataframe导入mysql
                try:
                    # pd.io.sql.to_sql(df1,tb_name1,con=connection,schema=db_name,if_exists='replace',index = False,index_label = False )
                    pd.io.sql.to_sql(df1,tb_name1,con=connection,schema=db_name,if_exists='replace',index = True,index_label = "Id" )
                except:
                    print('ERROR:cannot insert into mysql.')
                print('----table "'+tb_name1+'" finished----')
    
    end = datetime.datetime.now()
    print(end - start)


