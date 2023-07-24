#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 12 14:19:28 2023

@author: christopherharnett
"""

import numpy as np
import pandas as pd

df = pd.DataFrame({"VALUE1": [2, 4, np.nan, 6, np.nan, 8, 10],"VALUE2": [123, np.nan, 456, np.nan, 789, 246, 357],"VALUE3": ["India", "Canada", "USA", "Germany", "Sweden", "Norway", "Austria"]})

df

df.fillna(100000)
df

df["VALUE1"].fillna(100000)
df

df.mean()

df.fillna(df.mean())

df.fillna({"VALUE1": 100000, "VALUE2": 200000})

df["VALUE1"].fillna(df["VALUE2"].mean())

df["VALUE3"][0::2]

df["VALUE3"][0::2] = np.nan
df

df["VALUE3"].fillna("Siberia")
df

df.fillna(method="ffill")
df.fillna(method="pad")
df.fillna(method="bfill")
df.fillna(method="backfill")
