#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 17 00:10:16 2018

@author: yoon
"""

import numpy as np

arr_data1 = np.arange(1,10)
arr_data1

# 제곱근, 로그 : Data Scaling에 활용 가능
np.sqrt(arr_data1)
np.log10(arr_data1)

# 두 ndarray중 최대값으로 통합
x=np.random.randn(8)
y=np.random.randn(8)
np.maximum(x,y)

# series 데이터처럼 연산하기
arr_data2=np.random.randn(5,4)
arr_data2.sum()
arr_data2.mean()
arr_data2.sum(axis=0)
arr_data2>0
(arr_data2>0).sum()

# 정렬하기
arr_data3 = np.random.randn(8)
np.sort(arr_data3)
np.sort(arr_data3)[::-1]

arr_data4 = np.random.rand(5,3)
np.sort(arr_data4,axis=0)
np.sort(arr_data4,axis=1)

large_arr=np.random.rand(150)
np.sort(large_arr)[::-1]

# 상위 5%에 해당하는 index값 리턴하여, 최종적으로 5% 위치의 숫자 리턴
np.sort(large_arr)[::-1][int(0.05*len(large_arr))]

# unique 함수 사용
names=np.array(["Charles","Kilho","Hayoung","Charles","Hayoung","Kilho","Kilho"])
ints=np.array([3,3,3,2,2,1,1,4,4])
np.unique(names)
np.unique(ints)