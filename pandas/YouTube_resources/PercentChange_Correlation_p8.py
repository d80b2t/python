'''
https://www.youtube.com/watch?v=P90mCSsGE1c&index=8&list=PLQVvvaa0QuDc-3szzjeP6N6b0aDrrKyL-
https://pythonprogramming.net/percent-change-correlation-data-analysis-python-pandas-tutorial/?completed=/pickle-data-analysis-python-pandas-tutorial/
'''
import quandl
import pandas as pd
import pickle
import matplotlib.pyplot as plt
from matplotlib import style
style.use('fivethirtyeight')

api_key='xTrUFEADji37fXJVMPxM'

def state_list():
    fiddy_states = pd.read_html('https://simple.wikipedia.org/wiki/List_of_U.S._states')
    return fiddy_states[0][0][1:]

def grab_initial_state_data():
    states = state_list()
    main_df = pd.DataFrame()

    for abbv in states:
        query = "FMAC/HPI_"+str(abbv)
        print(query)
        
        df = quandl.get(query, authtoken=api_key)
        print(df.head())
        df.columns = [abbv]  ### This is the fix ###

        ## doing some manipulation on the DataFrame
        #df = df.pct_change()
        df[abbv] = (df[abbv] - df[abbv][0]) / df[abbv][0] *100
        
        if main_df.empty:
            main_df = df
        else:
            main_df = main_df.join(df)
            #eammain_df = main_df.join(df, lsuffix=abbv)  ### Could also do this ###

    print(main_df.head())
    
    pickle_out = open('fiddy_states3.pickle','wb')  ##write bytes
    pickle.dump(main_df, pickle_out)
    pickle_out.close()        
    ## Everything above here is in the function

    
def HPI_Benchmark():
    ## US-wide HPI 
    df_us = quandl.get("FMAC/HPI_USA", authtoken=api_key)
    ## Can do a df.head() to see what the columns are named
    print(df_us.head())
    #df_us.columns = ["United States"] ## This doesn't help
    #print(df_us[Value], df_us[Value][0])
    
    #df_us["United States"] = (df_us["United States"] - df_us["United States"][0]) / df_us["United States"][0] *100 ## Is given in the video, but doesn't work
    df_us["Value"] = (df_us["Value"] - df_us["Value"][0]) / df_us["Value"][0] *100
    
    return df_us ## critical line, duh!!! 

        
## Running this generates the new fiddy_*.pickle file
#grab_initial_state_data()


fig = plt.figure()
ax1 = plt.subplot2grid((1,1), (0,0))

#HPI_data = pd.read_pickle('pickle.pickle')
HPI_data = pd.read_pickle('fiddy_states3.pickle')

##  Modifying columns (and modifying columns within Pandas)
#HPI_data['TX2']  = HPI_data['TX']*2
#print(HPI_data[['TX', 'TX2']])

## Run the function..
benchmark = HPI_Benchmark()


#HPI_data.plot(ax=ax1, linewidth=1)
HPI_data.plot(ax=ax1, linewidth=2)
## for colors, b is blue, k is black
benchmark.plot(color='k',ax=ax1, linewidth=6, linestyle='--')

#HPI_data.plot()
plt.legend().remove()
plt.show()

## Let's create a correlation table. W00T W00T!!!
HPI_State_Correlation = HPI_data.corr()

## Noting HPI_State_Correlation is a dataframe...
##In [9]: type(HPI_State_Correlation)
##Out[9]: pandas.core.frame.DataFrame

print(HPI_State_Correlation)

print(HPI_State_Correlation.min)         ## print the 50x50... 
print(HPI_State_Correlation.min())       ## prints the min of each State...
# print(HPI_State_Correlation.min()[0])  ## gives the min for AL
# print(HPI_State_Correlation.min()[1])  ## gives the min for AK etc. 
# type(HPI_State_Correlation.min()[1])   ## is a numpy.float64

## Describe the detail, some top level-nos and stats...
print(HPI_State_Correlation.describe())


