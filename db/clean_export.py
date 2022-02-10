import pandas as pd
import sqlite3

df = pd.read_csv('db/covid_19_data.csv')

df.columns = ['SNo', 'ObservationDate', 'State', 'Country',
              'LastUpdate', 'Confirmed', 'Deaths', 'Recovered']

for i in df.columns:
    if df[str(i)].dtype == 'float64':
        df.fillna(0.0, inplace=True)
    else:
        df.fillna("UnKnown", inplace=True)

df['ObservationDate'] = pd.to_datetime(df['ObservationDate'])

df['LastUpdate'] = pd.to_datetime(df['LastUpdate'])

print(df.head(3))

df.to_csv("covid_clean_data.csv", index=False)

connection = sqlite3.connect('covid.db')

df.to_sql('covid', connection, if_exists='replace', index=False)

connection.close()

#makesure that database in folder where code is present
