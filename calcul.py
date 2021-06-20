import pandas as pd
df = pd.read_csv('https://epistat.sciensano.be/Data/COVID19BE_VACC.csv')
df = pd.pivot_table(df, index = 'DATE', columns = 'DOSE', values = 'COUNT', aggfunc = 'sum')
df['CumulA'] = df['A'] + df ['C']
df['CumulB'] = df['B'] + df ['C']
df['CumuleA'] = df['CumulA'].cumsum().map('{0:g}'.format)
df['CumuleB'] = df['CumulB'].cumsum().map('{0:g}'.format)
df.to_csv("./result.csv")
