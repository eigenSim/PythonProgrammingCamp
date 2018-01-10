#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  8 22:55:37 2018

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
stud_alcoh = df.loc[: , "school":"guardian"]
stud_alcoh.head()

# 익명함수 생성(일급객체로 활용)
captalizer = lambda x: x.upper()

# 범수형 변수 확인 및 대문자변환
stud_alcoh['Mjob'].value_counts()
stud_alcoh['Fjob'].value_counts()
stud_alcoh['Mjob'].apply(captalizer) # error case
stud_alcoh['Fjob'].apply(captalizer)
stud_alcoh['Mjob'] = stud_alcoh['Mjob'].apply(captalizer)
stud_alcoh['Fjob'] = stud_alcoh['Fjob'].apply(captalizer)

# 고차원 조건함수 생성
def majority(x):
    if x > 17:
        return True
    else:
        return False

# 익명함수를 조건으로 적용하여 새로운 피처 생성
stud_alcoh['legal_drinker'] = stud_alcoh['age'].apply(majority)
stud_alcoh.head()

# 고차원 조건함수 생성
def times10(x):
    if type(x) is str:
        return x
    elif type(x) is numpy.int64:
        return 10 * x
    else:
        return
    
# applymap은 바로 적용
stud_alcoh.applymap(times10).head(10)