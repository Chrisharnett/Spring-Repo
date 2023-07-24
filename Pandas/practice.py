#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 11 13:39:13 2023

@author: christopherharnett
"""

import pandas as pd
import numpy as np

np.random.seed(88)

df = pd.DataFrame(data = np.random.randn(18, 6), index = "R1 R2 R3 R4 R5 R6 R7 R8 R9 R10 R11 R12 R13 R14 R15 R16 R17 R18".split(), columns = "C1 C2 C3 C4 C5 C6".split())

df = pd.DataFrame(data = np.random.randn(10, 5), index = "A B C D E F G H I J".split(), columns = "VALUE1 VALUE2 VALUE3 VALUE4 VALUE5".split())
df                  

blockofdata = df.loc["R4":"R12", "C3":"C5"]
blockofdata = df.iloc[3:11, 2:5]
blockofdata
