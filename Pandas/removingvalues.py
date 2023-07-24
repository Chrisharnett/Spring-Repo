#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 12 13:13:23 2023

@author: christopherharnett
"""

import numpy as np
import pandas as pd

x = np.arange(0,28).reshape(7,4)

df = pd.DataFrame(data=x, columns="C1 C2 C3 C4".split())

df
""" displays without columns """
df.drop(["C1", "C2"], axis=1)
df

""" removes them from original df """
df.drop(["C1", "C2"], axis=1, inplace=True)
df

df.drop([2,5], axis=0, inplace=True)
df
