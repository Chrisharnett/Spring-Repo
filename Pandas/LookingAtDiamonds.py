#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on Wed Jul 19 13:33:33 2023

@author: christopherharnett
"""

import pandas as pd
import seaborn as sns
import warnings

warnings.filterwarnings('ignore')

df = sns.load_dataset('diamonds')
df.head()


df['price'].mean()

df['price'].max()

sns.displot(df['price'])

