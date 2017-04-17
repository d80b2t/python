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

#
# Table of Percentile points from 1 to 99 for total income before and after tax
#
path = 'Table_3_1a_14.xlsx'

# Open the workbook
workbook = xlrd.open_workbook(path)

# Choose the sheet 
sheet = workbook.sheet_by_index(0)


# Pick out the first column...
full_x = sheet.col_values(0)
# These are the Percentile points, 1 - 99 
percentile = full_x[11:110]
#
percentile = full_x[114:213]


# Total income BEFORE tax, in GBP
#  2 : for 1999-00
full_y = sheet.col_values(1)
#  3 ; for 2000-01
# 16 : for 2013-14
full_y = sheet.col_values(16)
income_before = full_y[11:110]


# Total income BEFORE tax, in GBP
income_after = full_y[114:213]

# from GBP into kGPB
income_before_tax = [income_before/1000. for income_before in income_before]
income_after_tax  = [income_after/1000. for income_after in income_after]


##
## http://people.duke.edu/~ccc14/pcfb/numpympl/MatplotlibBarPlots.html
##

#fig = plt.figure()
#ax = fig.add_subplot(111)
fig, ax = plt.subplots()

rects1 = ax.bar(percentile, income_before_tax, color='r')
rects2 = ax.bar(percentile, income_after_tax, color='b')

## axes and labels
#ax.set_xlim(-width,len(ind)+width)
#ax.set_ylim(0,45)
ax.set_xlabel('Percentiles')
ax.set_ylabel("Pounds, '000 ")
ax.set_title('Total income before and after tax (2013-14)')

## xTickMarks = ['Group'+str(i) for i in range(1,6)]
## ax.set_xticks(ind+width)
## xtickNames = ax.set_xticklabels(xTickMarks)
## plt.setp(xtickNames, rotation=45, fontsize=10)

## add a legend
ax.legend( (rects1[0], rects2[0]), ('Income before tax', 'Income after tax') )

plt.show()



