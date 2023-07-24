#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  5 14:01:04 2023

@author: christopherharnett

indexing and slicing
"""

import pandas as pd

indexSliceExample = pd.Series(["+91", "+49", "+33", "+39", "+46", "+1"], index = ["India", "Germany", "France", "Italy", "Sweden", "Canada"])


indexSliceExample["India"]
indexSliceExample[0]

""" slicing """

indexSliceExample[1:6:2]

indexSliceExample["Germany":"Sweden":2]

""" slicing backwards """

indexSliceExample[6:1:-1]

