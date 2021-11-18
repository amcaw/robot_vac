import pandas as pd
df_hospi = pd.read_csv ('https://epistat.sciensano.be/Data/COVID19BE_HOSP.csv')
df_hospi1 = df_hospi[['DATE', 'TOTAL_IN']]
df_hospi2 = df_hospi[['DATE', 'TOTAL_IN_ICU']]
df_hospi1 = df_hospi1.groupby(['DATE'], as_index=False)['TOTAL_IN'].sum()
df_hospi2 = df_hospi2.groupby(['DATE'], as_index=False)['TOTAL_IN_ICU'].sum()
df_hospi = pd.merge(df_hospi1, df_hospi2)
df_hospi['DATE'] = df_hospi['DATE'].tail(1)
df_hospi.dropna(subset = ['DATE'], inplace=True)
df_hospi.to_csv("./result_hospi.csv")
