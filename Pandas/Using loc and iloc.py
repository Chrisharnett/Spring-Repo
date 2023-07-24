#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul  6 12:52:41 2023

@author: christopherharnett
"""

import numpy as np
import pandas as pd

np.random.seed(88)

df = pd.DataFrame(data = np.random.randn(10, 5), index = "A B C D E F G H I J".split(), columns = "VALUE1 VALUE2 VALUE3 VALUE4 VALUE5".split())
df

df.loc["C":"G", "VALUE3"]
df.iloc[2:7, 2]

""" Gives us the results as a dataframe """
df.loc["C":"G", ["VALUE3"]]

df.loc["C":"G"][["VALUE3"]]

df.iloc[2:7]["VALUE3"]
