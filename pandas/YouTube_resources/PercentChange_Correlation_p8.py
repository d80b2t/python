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
    ## Can do a df.head()
    print(df_us.head())
    #df_us.columns = ["United States"]
    
    #print(df_us[Value], df_us[Value][0])
    #df_us["United States"] = (df_us["United States"] - df_us["United States"][0]) / df_us["United States"][0] *100
    df_us["Value"] = (df_us["Value"] - df_us["Value"][0]) / df_us["Value"][0] *100
    return df_us
        
## Running this generates the new fiddy_*.pickle file
#grab_initial_state_data()


fig = plt.figure()
ax1 = plt.subplot2grid((1,1), (0,0))

#HPI_data = pd.read_pickle('pickle.pickle')
HPI_data = pd.read_pickle('fiddy_states3.pickle')

##  Modifying columns (and modifying columns within Pandas)
#HPI_data['TX2']  = HPI_data['TX']*2
#print(HPI_data[['TX', 'TX2']])

## Let's create a correlation table. W00T W00T!!!
HPI_State_Correlation = HPI_data.corr()
print(HPI_State_Correlation)



benchmark = HPI_Benchmark()
HPI_data.plot(ax=ax1)
benchmark.plot(color='k',ax=ax1, linewidth=10)

#HPI_data.plot()
plt.legend().remove()
plt.show()


## doing things in "% change" :-)
