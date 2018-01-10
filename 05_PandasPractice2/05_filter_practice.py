#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  8 23:16:22 2018

@author: yoon
"""

import pandas as pd

# 깃헙 업로드 데이터 가져오기. 
# github.com 대신에 raw.githubusercontent.com 
# master/blob 에서 blob제거
url = 'https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/04_Apply/Students_Alcohol_Consumption/student-mat.csv'
df = pd.read_csv(url, sep=',')
df.head()

# 데이터 부분집합 추출
stud_alcoh1 = df.loc[: , "school":"guardian"]
stud_alcoh2 = df[['school', 'guardian']]

# 여러가지 필터링 방법
more_than_16 = stud_alcoh1[stud_alcoh1.age > 16]
contains_G = stud_alcoh1[stud_alcoh1.famsize.str.contains('G')] # startswith 등 활용가능
mother_job = stud_alcoh1.loc[stud_alcoh1.Mjob.isin(['at_home', 'services']), ['Mjob','Fjob', 'reason']]