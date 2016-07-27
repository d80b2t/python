'''

https://sites.google.com/site/aslugsguidetopython/data-analysis/pandas/pandas-example

'''

import numpy as np
import matplotlib as p
import pdb
from pandas import *

# Now we have to read in the data
data = read_csv('train.csv')

#print data

# This reads the data into a handy dataframe format. So that if we
# enter the command data we get a summary of the data's structure

'''
 This data has information on passengers from the Titanic disaster and
 is focused on the problem of using the various pieces of information
 to create a good predictor of if someone survived the sinking of the
 ship. One thing one might want to consider is whether the properties
 of the mens survival was different from the womens.
'''

# So we can create separate data frames for men and women as

men = data[data.Sex == 'male']
women = data[data.Sex =='female']
  
# We can then find the proportion of men and women that survive with the following commands
proportion_women_survived = float(sum(women.Survived))/len(women)
proportion_men_survived = float(sum(men.Survived))/len(men)


print data.Age
print men.Age
print women.Age

#You can access the column names with
print data.columns

#You can access a row with a cross-section (xs), in this case we choose the 0th row (replacing 0 with another index returns that row.
print data.xs(0)

data.pclass.hist()

