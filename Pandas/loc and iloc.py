#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul  6 12:43:04 2023

@author: christopherharnett

Using loc and Iloc
"""

import numpy as np
import pandas as pd

np.random.seed(88)

df = pd.DataFrame(data = np.random.randn(10, 5), index = "A B C D E F G H I J".split(), columns = "VALUE1 VALUE2 VALUE3 VALUE4 VALUE5".split())
df

df.loc["A":"D"]
df.iloc[0:4]

""" by row and column"""
df.loc["C", "VALUE4"]

df.iloc[2, 3]


