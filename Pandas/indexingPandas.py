#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 13 11:42:44 2023

@author: christopherharnett
"""

import numpy as np
import pandas as pd

np.random.seed(88)

df = pd.DataFrame(data = np.random.randn(10, 5), index = "A B C D E F G H I J".split(), columns = "VALUE1 VALUE2 VALUE3 VALUE4 VALUE5".split())
df

""" Change indexes of DF"""

""" Keeps previous index as new column"""
df.reset_index()

""" drop=True means no old index, inplace=Alter original table """
df.reset_index(drop=True, inplace=True)
df

example = "CA F IND AZ USA MEX ARG CH PAR PT".split()
example

df["new_index"] = example
df

df.set_index("new_index")
df

df.set_index("new_index", inplace=True)
df
