#!/usr/bin/env python

"""
https://www.youtube.com/watch?v=WlGq6R4U2gE

https://www.gov.uk/government/statistics/percentile-points-from-1-to-99-for-total-income-before-and-after-tax

https://www.gov.uk/government/statistics/distribution-of-median-and-mean-income-and-tax-by-age-range-and-gender-2010-to-2011
"""

import numpy as np
import matplotlib.pyplot as plt

import pyexcel as pe
import openpyxl as px
import numpy as np
import xlrd 


path = 'Table_3_1a_14.xlsx'

workbook = xlrd.open_workbook(path)

sheet = workbook.sheet_by_index(0)

#W = px.load_workbook('Table_3_1a_14.xlsx', use_iterators = True)
#p = W.get_sheet_by_name(name = 'Sheet1')

# These are the Percentile points
full_x = sheet.col_values(0)
x = full_x[11:110]

# 
full_y = sheet.col_values(16)
y = full_y[11:110]

#ind = np.arange(N)  # the x locations for the groups
#width = 0.35       # the width of the bars

fig, ax = plt.subplots()


rects1 = ax.bar(x, y, color='r')



