#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 13 11:55:11 2023

@author: christopherharnett
"""

import numpy as np
import pandas as pd

""" create inside labels first"""
inside = ["Class A", "Class B", "Class C", "Class A", "Class B", "Class C"]

""" Then outside labels"""
outside = ["CNA 1", "CNA 1", "CNA 1", "CNA 2", "CNA 2", "CNA 2"]


multi_index = list(zip(outside, inside))

 
higher_index = pd.MultiIndex.from_tuples(multi_index)
 higher_index

np.random.seed(88)

df = pd.DataFrame(np.random.randint(70, 100, size=(6,2)), index = higher_index, columns=["1st Semester", "2nd Semester"])
df

df["1st Semester"]
df[["1st Semester"]]
df[["2nd Semester"]]

df
df.loc["CNA 1"]

df.loc["CNA 1"].loc["Class B"]
df.loc["CNA 1"].loc[["Class B"]]

df.index

df.index.names


df.index.names = ["Campus", "Classes"]
df