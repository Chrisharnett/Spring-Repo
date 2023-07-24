#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 12 12:33:22 2023

@author: christopherharnett
"""

import numpy as np
import pandas as pd

np.random.seed(88)

df = pd.DataFrame(data = np.random.randn(10, 5), index = "A B C D E F G H I J".split(), columns = "VALUE1 VALUE2 VALUE3 VALUE4 VALUE5".split())
df

""" returns boolean if value > 0.5 """
df > 0.5

"""displays only values that fit the condition"""
df[df > 0.5]


df["VALUE1"] < 0.5

df[df["VALUE1"] < 0.5]

""" Show only items in Value2 that have VALUE1 values < 0.5 """

df[df["VALUE1"] < 0.5] ["VALUE2"]

""" Return above as a dataframe """
df[df["VALUE1"] < 0.5][["VALUE2"]]

""" Return multiple columns"""
df[df["VALUE1"] < 0.5][["VALUE2", "VALUE5"]]

""" AND condition """
df[(df["VALUE1"] > 0.5) & (df["VALUE4"] < 0.25)]

""" OR condition """
df[(df < 0.75) | (df["VALUE5"] > 0.5)]

df.loc[df.VALUE2 > 0.25, ["VALUE2", "VALUE3", "VALUE5"]]
