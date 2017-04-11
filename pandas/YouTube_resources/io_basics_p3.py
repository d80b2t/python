import pandas as pd


## http://pandas.pydata.org/pandas-docs/stable/io.html
df = pd.read_csv('ZILL-Z77006_MLP.csv')
#print(df.head())

df.set_index('Date', inplace=True)

## Write to a new csv file
#df.to_csv('new_csv2.csv')

df=pd.read_csv('new_csv2.csv')
#print(df.head())


## Specifying Date as the Index.
df=pd.read_csv('new_csv2.csv', index_col=0)
#print(df.head())

## Note Index is NOT a column!!
df.columns = ['Austin_HPI']
#print(df.head)
#print(df.head())

df.to_csv('new_csv3.csv')

df.to_csv('new_csv4.csv', header=False)

df = pd.read_csv('new_csv4.csv', names=['Date', 'Austin_HPI'], index_col=0)
print(df.head())

## Make and write to a .json file and format
df.to_json('new_json.json')

## Make and write to html (html table); very cool. 
df.to_html('example.html')

df = pd.read_csv('new_csv4.csv', names=['Date', 'Austin_HPI'])
print(df.head())

df.rename(columns={'Austin_HPI':'77006_HPI'}, inplace=True)
print(df.head())
