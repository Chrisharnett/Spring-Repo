#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  5 14:15:39 2023

@author: christopherharnett
"""

import pandas as pd

dataframeListEx = [5, 10, 15, 20, 25]

dataframeListEx

pd.DataFrame(data = dataframeListEx, columns=["values"], dtype="float")
