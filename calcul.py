import pandas as pd #yoo
from datetime import datetime
df = pd.read_csv ('https://epistat.sciensano.be/Data/COVID19BE_VACC.csv')
df = df[df.AGEGROUP != '00-11']
df = df[df.AGEGROUP != '12-15']
df = df[df.AGEGROUP != '16-17']
df = pd.pivot_table(df, index = 'DATE', columns = 'DOSE', values = 'COUNT', aggfunc = 'sum')
df['A'] = df['A'].fillna(0)
df['B'] = df['B'].fillna(0)
df['C'] = df['C'].fillna(0)
df['E'] = df['E'].fillna(0)
df['CumuleA'] = df['A'].cumsum()
df['CumuleB'] = df['B'].cumsum()
df['CumuleC'] = df['C'].cumsum()
df['CumuleC'] = df['CumuleC'].fillna(0)
df['CumuleE'] = df['E'].cumsum()
df['CumuleE'] = df['CumuleE'].fillna(0)
df['A'] = df.apply(lambda x: x['CumuleA'] + x['CumuleC'], axis=1)
df['B'] = df.apply(lambda x: x['CumuleB'] + x['CumuleC'], axis=1)
df['E'] = df['CumuleE']
df.to_csv("./result.csv")
