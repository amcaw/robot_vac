import pandas as pd
from datetime import datetime
df = pd.read_csv ('https://epistat.sciensano.be/Data/COVID19BE_VACC.csv')
df = pd.pivot_table(df, index = 'DATE', columns = 'DOSE', values = 'COUNT', aggfunc = 'sum')
df['CumuleA'] = df['A'].cumsum().map('{0:g}'.format)
df['CumuleB'] = df['B'].cumsum().map('{0:g}'.format)
df['CumuleC'] = df['C'].cumsum().map('{0:g}'.format)
df['A'] = df['CumuleA'] + df['CumuleC']
df['B'] = df['CumuleB'] + df['CumuleC']
df.to_csv("./result.csv")
