import pandas as pd
import sqlite3

df = pd.read_csv('db/covid_19_data.csv')

# print(df.head(3))

# df.drop(columns=['SNo'],axis=1,inplace=True)

# df.rename(columns={"State":"Province/State","Country":"Country/Region",
#                    "LastUpdate":"Last Update"},inplace=True)

df.columns = ['SNo', 'ObservationDate', 'State', 'Country',
              'LastUpdate', 'Confirmed', 'Deaths', 'Recovered']

print(df.head(3))

for i in df.columns:
    if df[str(i)].dtype == 'float64':
        df.fillna(0.0, inplace=True)
    else:
        df.fillna("UnKnown", inplace=True)

# df.to_csv("db/covid_clean_data.csv",index=False)

connection = sqlite3.connect('covid.db')

df.to_sql('covid', connection, if_exists='replace', index=False)

for row in connection.execute('SELECT * FROM covid'):
    print(row)

connection.close()
