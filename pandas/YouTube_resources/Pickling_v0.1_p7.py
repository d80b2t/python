'''
https://www.youtube.com/watch?v=WkIW0YLoQEE&list=PLQVvvaa0QuDc-3szzjeP6N6b0aDrrKyL-&index=7
https://pythonprogramming.net/pickle-data-analysis-python-pandas-tutorial/?completed=/join-merge-data-analysis-python-pandas-tutorial/

'''
import quandl
import pandas as pd

## I have my Quandl API Key in quandlapikey.txt
api_key = open('quandlapikey.txt','r').read()

fiddy_states = pd.read_html('https://simple.wikipedia.org/wiki/List_of_U.S._states')

apikey='xTrUFEADji37fXJVMPxM'
for abbv in fiddy_states[0][0][1:]:
    #print("FMAC/HPI_"+str(abbv))
    query="FMAC/HPI_"+str(abbv)
    #df = quandl.get(query) ## Times out; too many requests (>20 in 10mins)
    #df = quandl.get(query, authtoken=api_key)
    ## yeah, I get a::
    ##  ValueError: Invalid header value b'xTrUFEADji37fXJVMPxM\n'
    ## here; guessing it's something to do with how open().read() works...
    
    df = quandl.get(query, authtoken=apikey)


    
    
    
    
    
