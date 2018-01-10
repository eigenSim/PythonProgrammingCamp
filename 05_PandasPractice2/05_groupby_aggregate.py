#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  8 22:22:07 2018

@author: yoon
"""

import pandas as pd
import numpy as np

url = 'https://raw.githubusercontent.com/justmarkham/DAT8/master/data/chipotle.tsv'
chipo = pd.read_csv(url, sep = '\t')

# 달러 타입 변환하기
chipo['item_price'] = chipo['item_price'].apply(lambda x: float(x[1:]))

# groupby와 관련된 연산 사용하기
chipo_pricediff = chipo.groupby('order_id')['item_price'].agg(np.ptp)
df = chipo_pricediff.to_frame().reset_index()
df = df.rename(columns={'item_price': 'item_price_diff'})
result_data = pd.merge(chipo, df, on='order_id', how='outer')

chipo_counts = chipo.groupby('order_id').aggregate(sum).reset_index()
chipo_counts = chipo_counts.rename(columns={'quantity': 'quantity_sum', 'item_price': 'item_price_sum'})
result_data2 = pd.merge(chipo, chipo_counts, on='order_id', how='outer')