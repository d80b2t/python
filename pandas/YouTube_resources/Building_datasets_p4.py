'''
https://www.youtube.com/watch?v=3GpvWlVinf0&index=4&list=PLQVvvaa0QuDc-3szzjeP6N6b0aDrrKyL-
https://pythonprogramming.net/dataset-data-analysis-python-pandas-tutorial/?completed=/input-output-data-analysis-python-pandas-tutorial/

Also::
https://www.quandl.com/tools/python
http://help.quandl.com/article/205-how-do-i-download-a-dataset-using-python

'''
import quandl
import pandas as pd

# Not necessary, do this so you do not show my API key
api_key = open('quandlapikey.txt','r').read()

#df = quandl.get("FMAC/HPI_TX", authtoken=api_key)
df = quandl.get("FMAC/HPI_TX")
#print(df.head())


fiddy_states = pd.read_html('https://simple.wikipedia.org/wiki/List_of_U.S._states')
## this is gonna be a whole **list** of DataFrames
#print(fiddy_states)

## This is a DataFrames
#print(fiddy_states[0])

## And now we want column zero... is a DataFrames
print(fiddy_states[0][0])

## Of column zero, we want everything from row one onward...
for abbv in fiddy_states[0][0][1:]:
    print("FMAC/HPI_"+str(abbv))
