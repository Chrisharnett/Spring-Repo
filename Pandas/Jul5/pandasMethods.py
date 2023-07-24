#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  5 13:41:30 2023

@author: christopherharnett

methods of Pandas
"""

import pandas as pd

appliedExample = pd.Series([8, 3, 6, 5, 1], index = ["b", "d", "c", "a", 'e'])

appliedExample

""" order by index """
indexSortAppliedEx = appliedExample.sort_index()

indexSortAppliedEx

""" order by values """

valueSortAppliedEx = appliedExample.sort_values()
valueSortAppliedEx

""" sorting different data types not supported"""
dtypeList = pd.Series(["string", True, 12, 4.334])
sortIndexDtype = dtypeList.sort_index()
sortIndexDtype
sortedTypeList = dtypeList.sort_values()

""" search for a value """

appliedExample.isin([3, 5]) """either 3 or 5"""

appliedExample[appliedExample.isin([3,5])] """ displays values that match """

""" accessing the values"""
appliedExample.values """ outputs an array of the values """
valuesList = [i for i in appliedExample.values]

""" index method """
appliedExample.index
[i for i in appliedExample.index]

""" items method access index and value """
appliedExample.items

appliedExample.items()

list(appliedExample.items())

for index, value in appliedExample.items():
    print(index + " - ", + value)
