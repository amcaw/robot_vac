import pandas as pd
from datetime import datetime
df = pd.read_csv ('https://epistat.sciensano.be/Data/COVID19BE_VACC.csv')
df = pd.pivot_table(df, index = 'DATE', columns = 'DOSE', values = 'COUNT', aggfunc = 'sum')
df['CumuleA'] = df['A'].cumsum().map('{0:g}'.format).fillna(0)
df['CumuleB'] = df['B'].cumsum().map('{0:g}'.format).fillna(0)
df['CumuleC'] = df['C'].cumsum().map('{0:g}'.format).fillna(0)
df['DoseA'] = df['CumuleA'] + df['CumuleC']
df['DoseB'] = df['CumuleB'] + df['CumuleC']
df.to_csv("./result.csv")
