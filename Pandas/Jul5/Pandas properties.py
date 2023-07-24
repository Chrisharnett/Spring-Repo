#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  5 14:20:49 2023

@author: christopherharnett
"""

import pandas as pd
import random

x = random.sample(range(1, 99), 6)
x

y = random.sample(range(1, 99), 6)
z = random.sample(range(1, 99), 6)
a = random.sample(range(1, 99), 6)
b = random.sample(range(1, 99), 6)

dictData = {"val1": x, "val2": y, "val4": z, "val5": a, "val6": b}
dictData

df = pd.DataFrame(dictData)
df

df.head()
df.head(3)

df.tail()
df.tail(2)

""" returns columns names"""

df.columns

[i for i in df.columns]

df.columns = ["new1", "new2", "new3", "new4", "new5"]
df

df.values

[i for i in df.values]

type(df)

df.shape

df.ndim

df.size
