'''
https://www.youtube.com/watch?v=WkIW0YLoQEE&list=PLQVvvaa0QuDc-3szzjeP6N6b0aDrrKyL-&index=7
https://pythonprogramming.net/pickle-data-analysis-python-pandas-tutorial/?completed=/join-merge-data-analysis-python-pandas-tutorial/


 K e y   N o t e s::
https://pythonprogramming.net/community/143/Problem%20(and%20solution)%20to%20a%20pandas%20join%20issue%20in%20data%20analysis%20tutorial/
http://stackoverflow.com/questions/26645515/pandas-join-issue-columns-overlap-but-no-suffix-specified
http://stackoverflow.com/questions/26027877/join-two-dataframes-on-one-key-column-error-columns-overlap-but-no-suffix-sp

'''
import quandl
import pandas as pd
import pickle

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
        df.columns = [abbv]  ### This is the fix ###

        if main_df.empty:
            main_df = df
        else:
            main_df = main_df.join(df)
            #eammain_df = main_df.join(df, lsuffix=abbv)  ### Could also do this ###

    print(main_df.head())
    
    pickle_out = open('fiddy_states.pickle','wb')  ##write bytes
    pickle.dump(main_df, pickle_out)
    pickle_out.close()        


grab_initial_state_data()

    
    
    
    
