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
