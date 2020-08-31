#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/4/14 15:00
# @Author  : JackFeng
# @FileName: FakerData.py
# @Software: PyCharm
# @Blog    ：http://www.a2data.cn/


"""

安装相关包：  pip install Faker

Faker 提供了一个工厂函数，用来创建数据
当然，需要创建一个 Faker类来创建实例


选项说明：
faker ： 在shell中，faker 命令也可以用 python -m faker 来代替
-h，–help ： 帮助信息
–version ：显示版本
-o filename ：输出结果到文件中
-l {bg_BG,cs_CZ,…,zh_CN,zh_TW} ：指定本地化，zh_CN 表示中文
-r REPEAT ：指定生成多少条相同类型的数据
-s SEP ：在每个输出后边添加指定的分隔符
-i {my.custom_provider other.custom_provider} ：自定义扩展，prividers列表。注意，这里要指定包含你 provider 类的模块的路径，而不是程序本身。
fake ：指定方法名称，如：name , address , text 等
[fake argument …] ：为方法指定参数。如上例，为 profile 方法指定 ssn 和 name 参数，只输出这两个类型的内容。

自定义生成器方法，生成随机数，手机号，以及连续数字等

"""
from builtins import range

from faker import Factory
import random
import csv 
f = open('pools/majors.csv', 'r')

# 创建实例
fake =Factory.create("zh_CN")


class Person():
    def name():
        """
        :return: 随机姓名
        """
        return fake.name()

    def Xin():
        """
        :return: 姓
        """
        return fake.last_name()
    def Ming():
        """
        :return: 名
        """
        return fake.first_name()
    def MaleName():
        """
        fake.last_name_male() # 男性姓
        fake.first_name_male() # 男性名
        :return: 男 姓名
        """
        return  fake.name_male()
    def FemaleName():
        """
        :return:  女姓名
        """
        return fake.name_female()

    def Phone():
        """
        fake.phonenumber_prefix() # 运营商号段，手机号码前三位
        :return: 随机手机号
        """
        return fake.phone_number()

    def Address():
        """
        :return: 地址
        """
        return fake.address()

    def SSN():
        """
        :return: 随机生成身份证号(18位)
        """
        return fake.ssn()

    def Email():
        """
        fake.safe_email() # 安全邮箱
        :return: Email
        """
        return fake.email()

    def Ipv4():
        """
        fake.ipv6(network=False)  # ipv6地址

        fake.uri() # uri
        :return:        IPV4地址
        """
        return fake.ipv4()

    def url():
        """
        fake.uri_path(deep=None) # uri路径
        fake.uri_extension() # uri扩展名
        fake.uri() # uri
        fake.mac_address() # MAC地址
        fake.user_agent() # UA
        :return:# url
        """
        return fake.url()

    def company():
        """
        fake.company_suffix() # 公司名后缀
        fake.company_email()  # 公司邮箱
        :return: 公司名
        """
        return fake.company()
    def job():
        """
        :return: 工作职位
        """
        return fake.job()
    def uuid():
        """
        :return: 返回随机uuid
        """
        return fake.uuid4()
    def card():
        """
        fake.credit_card_expire() # 卡的有效期
        fake.credit_card_provider(card_type=None) # 卡的提供者
        fake.credit_card_security_code(card_type=None)# 卡的安全密码
        fake.credit_card_full(card_type=None) # 完整卡信息
        fake.currency_code()  # 货币代码
        :return: 银行卡号
        """
        return fake.credit_card_number(card_type=None)


class DateClassify():

    def date_time():
        """
        :return: 随机日期时间
        """
        return fake.date_time(tzinfo=None)

    def ThisDate():
        """
        fake.month() # 随机月份
        fake.month_name() # 随机月份名字
        fake.day_of_week() # 随机星期几
        fake.iso8601(tzinfo=None) # 以iso8601标准输出的日期
        fake.date_time_this_year(before_now=True, after_now=False, tzinfo=None) # 本年的某个日期
        fake.date_time_between(start_date="-30y", end_date="now", tzinfo=None)  # 两个时间间的一个随机时间
        :return: 本月的某个日期
        """
        return fake.date_time_this_month(before_now=True, after_now=False, tzinfo=None)

    def Time():
        """
         fake.timezone() # 时区
         fake.date(pattern="%Y-%m-%d") # 随机日期（可自定义格式）
         fake.unix_time() # 随机unix时间（时间戳）
         fake.time_object() # 随机时间对象
         fake.time_delta() # 随机时间延迟
        :return: 时间
        """
        return fake.time(pattern="%H:%M:%S")


class PyMock():

    def pyint():
        """
        fake.pyfloat(left_digits=None, right_digits=None, positive=False)  # 浮点数
        fake.pydecimal(left_digits=None, right_digits=None, positive=False)  # 随机高精度数

        :return:随机int
        """
        return fake.pyint()

    def randomMxStr(min_chars=1, max_chars=18):
        """
        Max 与 Min 之间的随机字符串
        :return:
        """
        return fake.pystr(min_chars=min_chars, max_chars=max_chars)

    def randomList():
        """
        :return:随机生成一个list
        """
        return fake.pylist(nb_elements=10, variable_nb_elements=True )
    def profile():
        """

        :return:人物描述信息：姓名、性别、地址、公司等
        """
        return fake.profile(fields=None, sex=None)
    def profile1():
        """
        解析操作
        s = fake.simple_profile(sex="m")
        for i,v in s.items():
            print(i,v)
        :return: # 人物精简信息
        """
        return fake.simple_profile(sex="m")
    def browser():
        """
        浏览器
        fake.internet_explorer() # IE浏览器
        fake.opera() # opera浏览器
        fake.firefox() # firefox浏览器
        fake.safari() # safari浏览器
        fake.chrome() # chrome浏览器
        :return: google 浏览器
        """
        list = [fake.internet_explorer(),fake.opera(),fake.chrome(),fake.firefox()]

        return  random.choice(list)

    def platform():
        """
        fake.linux_platform_token() # linux
        fake.linux_processor() # linux 型号
        fake.windows_platform_token() # windows
        fake.mac_platform_token() # mac
        :return:
        """
        list = [fake.linux_platform_token(),fake.windows_platform_token(),fake.mac_platform_token()]
        return  random.choice(list)

    def mobile_user():
        """
        Faker常用 命令行
        faker address
        python3 -m faker address
        faker profile
        faker profile ssn,name
        faker -r=3 -s=";" name
        :return:
        """
        return  fake.pyint(),fake.simple_profile(sex="m")



class Student():
    def student_id():
        """
        :return: 随机7位学号
        """
        return fake.random_number(digits=7)

    def major():
        csvreader = csv.reader(f)
        majors = list(major for major in csvreader)
        return str(random.choice(majors))
    
#print(Student.major())



# def factory_generate_ids(starting_id=1, increment=1):
#     """ 返回一个生成器函数，调用这个函数产生生成器，从starting_id开始，步长为increment。 """
#
#     def generate_started_ids():
#         val = starting_id
#         local_increment = increment
#         while True:
#             yield val
#             val += local_increment
#
#     return generate_started_ids



# values =[1,2,3,4,5,6]
# def factory_choice_generator(values):
#     """ 返回一个生成器函数，调用这个函数产生生成器，从给定的list中随机取一项。 """
#
#     def choice_generator():
#         my_list = list(values)
#         rand = random.Random()
#         while True:
#             yield random.choice(my_list)
#
#     return choice_generator

#print('-----')
#print (PyMock.mobile_user())
#print('-----')
#print(Person.name())
#print(type(Person.name()))


"""
    1、配置文件
        MySQL链接信息 
        数据库 a2data datascience
        数据表（字段） tb1,tb2
    2、生成条数 
    3、字段名（值） 
    4、存入mysql数据库

"""










