#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  5 12:58:33 2023

@author: christopherharnett

How to create a panda series using a dictionary Data structure
"""

import pandas as pd

exampleDict = {"bmw": 333.3, "porsche": 336.8, "maserati": 358}
exampleDict

pd.Series(data = exampleDict)

testVar = pd.Series(data = exampleDict, index = ["maserati", "bmw", "lambourghini"])
testVar
