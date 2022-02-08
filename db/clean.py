import pandas as pd

df=pd.read_csv('db/covid_19_data.csv')

print(df.head(3))

df.drop(columns=['SNo'],axis=1,inplace=True)


for i in df.columns:
    if df[str(i)].dtype=='float64':
        df.fillna(0.0,inplace=True)
    else:
        df.fillna("UnKnown",inplace=True)

df.to_csv("db/covid_clean_data.csv",index=False)