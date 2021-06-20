import pandas as pd
df = pd.read_csv('https://epistat.sciensano.be/Data/COVID19BE_VACC.csv')
df = pd.pivot_table(df, index = 'DATE', columns = 'DOSE', values = 'COUNT', aggfunc = 'sum')
df['CumulA'] = df['A'].cumsum().map('{0:g}'.format)
df['CumulB'] = df['B'].cumsum().map('{0:g}'.format)
df['CumulC'] = df['C'].cumsum().map('{0:g}'.format)
df['CumuleA'] = df['CumulA'] + df['CumulC']
df['CumuleB'] = df['CumulB'] + df['CumulC']   
df.to_csv("./result.csv")
