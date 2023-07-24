#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 12 14:10:54 2023

@author: christopherharnett
"""

import numpy as np
import pandas as pd

df = pd.DataFrame({"VALUE1": [2, 4, np.nan, 6, np.nan, 8, 10],"VALUE2": [123, np.nan, 456, np.nan, 789, 246, 357],"VALUE3": ["India", "Canada", "USA", "Germany", "Sweden", "Norway", "Austria"]})

df

df.dropna()
df.dropna(axis=1)

df["VALUE4"] = np.nan
df

df.dropna(how='all')

df.dropna(how='all', axis=1, inplace=True)
df
