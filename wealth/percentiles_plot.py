

import pyexcel as pe
import openpyxl as px
import numpy as np
import xlrd 

path = 'Table_3_1a_14.xlsx'
workbook = xlrd.open_workbook(path)


#W = px.load_workbook('Table_3_1a_14.xlsx', use_iterators = True)
#p = W.get_sheet_by_name(name = 'Sheet1')
