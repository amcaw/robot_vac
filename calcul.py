import pandas as pd
from datetime import datetime
df = pd.read_csv ('https://epistat.sciensano.be/Data/COVID19BE_VACC.csv')
df = pd.pivot_table(df, index = 'DATE', columns = 'DOSE', values = 'COUNT', aggfunc = 'sum')
df['CumuleA'] = df['A'].cumsum().map('{0:g}'.format)
df['CumuleB'] = df['B'].cumsum().map('{0:g}'.format)
df['CumuleC'] = df['C'].cumsum().map('{0:g}'.format)
df['DoseA'] = df['CumuleA'].add(df['CumuleC'], fill_value=0)
df['DoseB'] = df['CumuleB'].add(df['CumuleC'], fill_value=0)
df.to_csv("./result.csv")
