'''
Pandas Indexing in dataframe
'''
import pandas as pd
data = {
    'id': [1, 2, 3, 4, 5, 6, 7],
    'name': ['jim', 'dwight', 'micheal', 'pam', 'angela', 'kevin', 'oscar'],
    'sal': [2000, 3000, 5000, 800, 3500, 1000, 2500],
    'city': ['NY', 'NJ', 'NM', 'NY', 'TX', 'CA', 'IL']
}
df_emp = pd.DataFrame(data)
print(df_emp)

res_df = df_emp.loc[((df_emp['sal'] > 2000) & (
    df_emp['city'] == 'NJ')), ['name', 'sal', 'city']]

print(res_df)
