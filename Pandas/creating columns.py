#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 12 12:59:47 2023

@author: christopherharnett
"""

import numpy as np
import pandas as pd

x = np.arange(0, 28).reshape(7,4)
x

df = pd.DataFrame(data = x, columns="C1 C2 C3 C4".split())

df["C5"] = df["C1"] + df["C2"]
df

df["C6"] = df["C3"] * df["C5"]
df

np.arange(28, 35)

df["C8"] = [35, 36, 37, 38, 39, 40, 41]
