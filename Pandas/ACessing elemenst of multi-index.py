#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 13 12:42:16 2023

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

""" Get a crosssection of Multi Index DF """
df.xs("CNA 2")
df.xs(("CNA 2", "Class A"))

df.index.names = ["Campus", "Classes"]
df
df.xs(("CNA 2", "Class A"), level = [0,1])
df.xs("Class A", level="Classes")
df.xs("Class A", level=1)

