import pandas as pd #yoo
from datetime import datetime
df = pd.read_csv ('https://epistat.sciensano.be/Data/COVID19BE_VACC.csv')
df = df[df.AGEGROUP != '00-11']
df = df[df.AGEGROUP != '12-15']
df = df[df.AGEGROUP != '16-17']
df = pd.pivot_table(df, index = 'DATE', columns = 'DOSE', values = 'COUNT', aggfunc = 'sum')
df['CumuleA'] = df['A'].cumsum()
df['CumuleB'] = df['B'].cumsum()
df['CumuleC'] = df['C'].cumsum()
df['A'] = df.apply(lambda x: x['CumuleA'] + x['CumuleC'], axis=1)
df['B'] = df.apply(lambda x: x['CumuleB'] + x['CumuleC'], axis=1)
df.to_csv("./result.csv")
