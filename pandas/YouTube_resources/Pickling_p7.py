'''
https://www.youtube.com/watch?v=WkIW0YLoQEE&list=PLQVvvaa0QuDc-3szzjeP6N6b0aDrrKyL-&index=7
https://pythonprogramming.net/pickle-data-analysis-python-pandas-tutorial/?completed=/join-merge-data-analysis-python-pandas-tutorial/

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
        df = Quandl.get(query, authtoken=api_key)
        print(query)
        
        if main_df.empty:
            main_df = df
        else:
            main_df = main_df.join(df)
            
    pickle_out = open('fiddy_states.pickle','wb')  ##write bytes
    pickle.dump(main_df, pickle_out)
    pickle_out.close()        

  
grab_initial_state_data()

    
    
    
    
