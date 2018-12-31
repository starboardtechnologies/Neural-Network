#Tip: mainly going to use Pandas for reading into .csv files

#Pandas
#%%

import pandas as pd

#Use pwd to navigate to which ever directory you are in.
#Almost every .csv file has a '.csv' extension, but not all.
#Use Tab to autocomplete which .csv file you should be using.
#If the .csv file isn't being generated via auto-complete after using Tab, the file probably isn't in the same directory as the Jupyter Notebook.

df = pd.read_csv('salaries.csv')

#  df = dataframe

#Returns back salary column.

df['Salary']

#Returns a list of column names.

df[['Salary', 'Name']]

#  .max

df['Salary'].max()

#  .describe

df.describe()

#  >  or <

df['Salary']  > 30000

#  myfilter

myfilter = df['Salary'] > 30000
df[df['Salary'] > 30000]

#  .as_matrix()

df.as_matrix()