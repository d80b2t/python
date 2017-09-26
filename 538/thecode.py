'''
https://www.dataquest.io/blog/making-538-plots/?utm_campaign=Data%2BElixir&utm_medium=web&utm_source=Data_Elixir_148
'''

import pandas as pd

#direct_link = 'http://www.randalolson.com/wp-content/uploads/percent-bachelors-degrees-women-usa.csv'
datafile='percent-bachelors-degrees-women-usa.csv'
women_majors = pd.read_csv(datafile)

print(women_majors.info())
print(women_majors.head())
print(women_majors.tail())

## Use .loc, a label-based indexer, to:
##  select the first row (the one that corresponds to 1970);
##  select the items in the first row only where the values are less
##   than 20; the Year field will be checked as well, but will obviously
##   not be included because 1970 is much greater than 20.
under_20 = women_majors.loc[0, women_majors.loc[0] < 20]
print(under_20)

under_20_graph = women_majors.plot(x = 'Year', y = under_20.index, figsize = (12,8))
print('Type:', type(under_20_graph))
