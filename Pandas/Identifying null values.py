#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 12 13:44:36 2023

@author: christopherharnett
"""

import numpy as np
import pandas as pd

df = pd.DataFrame({"VALUE1": [2, 4, np.nan, 6, np.nan, 8, 10],"VALUE2": [123, np.nan, 456, np.nan, 789, 246, 357],"VALUE3": ["India", "Canada", "USA", "Germany", "Sweden", "Norway", "Austria"]})

df
df.isnull()

len(df)

df.isnull().sum() / len(df *100)

df.notnull()
df.notnull().sum()
df.notnull().sum().sum()

df["VALUE1"].notnull()
df[df["VALUE1"].notnull()]
df

""" any == at least one"""
df.isnull().any()

df.isnull().any(axis=1)

condition = df.isnull().any(axis=1)

df[condition]

df[~condition]

""" .all = all match condition """

df.notnull().all()
