#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  8 23:36:47 2018

@author: yoon
"""

import pandas as pd

drinks = pd.read_csv('https://raw.githubusercontent.com/justmarkham/DAT8/master/data/drinks.csv')
drinks.head()

# 전체 평균보다 많은 알코올을 섭취하는 대륙 구하기
total_mean = drinks.total_litres_of_pure_alcohol.mean()
continent_mean = drinks.groupby('continent').total_litres_of_pure_alcohol.mean()
continent_over_mean = continent_mean[continent_mean >= total_mean]

# 전체 평균보다 적은 알코올을 섭취하는 대륙 중에서, spirit을 가장 많이 마시는 국가 구하기
total_mean = drinks.total_litres_of_pure_alcohol.mean()
continent_mean = drinks.groupby('continent').total_litres_of_pure_alcohol.mean()
continent_under_mean = continent_mean[continent_mean <= total_mean].index.tolist()
df_continent_under_mean = drinks.loc[drinks.continent.isin(continent_under_mean)]
b = df_continent_under_mean.loc[df_continent_under_mean['spirit_servings'].idxmax()]

# total_servings 칼럼 만들어서 병합하기
drinks['total_servings'] = drinks['beer_servings'] + drinks['wine_servings'] + drinks['spirit_servings']

# 평균 beer_servings이 가장 높은 대륙 구하기
beer_continent = drinks.groupby('continent').beer_servings.mean().idxmax()

# 대륙별 평균 wine_servings 칼럼 만들어서 병합하기
result = drinks.groupby('continent').mean()['wine_servings']
df = result.to_frame().reset_index()
df = df.rename(columns={'wine_servings': 'wine_servings_avg'})
new_df = pd.merge(drinks, df, on='continent', how='outer')

# 대륙별 spirit_servings의 평균, 최소, 최대, 합계 구하기
result = drinks.groupby('continent').spirit_servings.agg(['mean', 'min', 'max', 'sum'])