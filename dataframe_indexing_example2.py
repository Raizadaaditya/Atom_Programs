'''
data indexing example 2
'''

import pandas as pd
data = {
    'name': ['ram', 'sham', 'jerry'],
    'age': [10, 20, 15],
    'dept': ['A', 'B', 'A']
}

df = pd.DataFrame(data)
print(df)  # getting dataframe

print(df['name'])  # getting particular column of dataframe

# conditional indexing using .loc function
print(df.loc[(df['age'] > 10), ['name', 'age']])

# adding new column and adding values to new column
df.loc[(df['dept'] == 'A'), ['salary']] = 40000

print(df)
