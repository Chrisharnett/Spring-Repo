#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul  6 12:06:42 2023

@author: christopherharnett
"""

import numpy as np
import pandas as pd

np.random.seed(88)

df = pd.DataFrame(data = np.random.randn(6, 5), index = "A B C D E F".split(), columns = "VALUE1 VALUE2 VALUE3 VALUE4 VALUE5".split())
df

df[["VALUE2", "VALUE5"]]

variable = ["VALUE3", "VALUE4"]

df[variable]

df[["VALUE2", "VALUE5"]]


df[variable]["B":"D"]

df["B":"D"]

df[1:4]

df[1:2]

df["E":"E"]

df["E":"E"][["VALUE2", "VALUE4"]]


