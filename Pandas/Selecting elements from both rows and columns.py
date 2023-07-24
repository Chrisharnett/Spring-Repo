#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul  6 13:04:50 2023

@author: christopherharnett
"""

import numpy as np
import pandas as pd

np.random.seed(88)

df = pd.DataFrame(data = np.random.randn(10, 5), index = "A B C D E F G H I J".split(), columns = "VALUE1 VALUE2 VALUE3 VALUE4 VALUE5".split())
df

""" Getting blocks of data """

df.loc["C":"H", "VALUE2":"VALUE4"]
df.iloc[2:8, 1:4]


df.iloc[2:8, 1:4].loc["E":"F", ["VALUE3"]]
df.iloc[2:8, 1:4].iloc[2:4, [1]]
