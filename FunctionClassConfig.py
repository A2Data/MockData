#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 18:53:42 2020

@author: kath
"""


#字典传参数1-识别Function-字段名:函数名
dict1 = {
    'SSN' : 'SSN',
    'name' : 'name',
    'admission_date' : 'admission_date',
    'contact' : 'contact',
    'Xin' : 'Xin',
    'Ming' : 'Ming',
    'MaleName' : 'MaleName',
    'FemaleName' : 'FemaleName',
    'Phone' : 'Phone',
    'Address' : 'Address',
    'Email' : 'Email',
    'Ipv4' : 'Ipv4',
    'url' : 'url',
    'company' : 'company',
    'job' : 'job',
    'uuid' : 'uuid',
    'card' : 'card',
    'date_time' : 'date_time',
    'ThisDate' : 'ThisDate',
    'Time' : 'Time',
    'pyint' : 'pyint',
    'randomMxStr' : 'randomMxStr',
    'randomList' : 'randomList',
    'profile' : 'profile',
    'profile1' : 'profile1',
    'browser' : 'browser',
    'platform' : 'platform',
    'mobile_user' : 'mobile_user',
    'student_id':'student_id',
    'major':'major',
    }
#字典传参数2-识别Class-函数名:类名
dict2 = {
    'name' : 'Person',
    'Xin' : 'Person',
    'Ming' : 'Person',
    'MaleName' : 'Person',
    'FemaleName' : 'Person',
    'Phone' : 'Person',
    'Address' : 'Person',
    'SSN' : 'Person',
    'Email' : 'Person',
    'Ipv4' : 'Person',
    'url' : 'Person',
    'company' : 'Person',
    'job' : 'Person',
    'uuid' : 'Person',
    'card' : 'Person',
    'date_time' : 'DateClassify',
    'ThisDate' : 'DateClassify',
    'Time' : 'DateClassify',
    'pyint' : 'PyMock',
    'randomMxStr' : 'PyMock',
    'randomList' : 'PyMock',
    'profile' : 'PyMock',
    'profile1' : 'PyMock',
    'browser' : 'PyMock',
    'platform' : 'PyMock',
    'mobile_user' : 'PyMock',
    'student_id':'Student',
    'major':'Student',
    }
def findFunction(a):
    return dict1[a]             #返回str

def findClass(a):
   return dict2[a]