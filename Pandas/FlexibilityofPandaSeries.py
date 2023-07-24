#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  5 13:07:47 2023

@author: christopherharnett


"""

import pandas as pd

series = pd.Series(["cna", 100, 2.0, True])

series[0]

type(series[3])
print(type(series[3]))

pd.Series([sum, type, min])
