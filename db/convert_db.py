import sqlite3
import csv

connection = sqlite3.connect('cdata.db')

cursor = connection.cursor()

create_table = '''CREATE TABLE covid(
    ObservationDate DATE NOT NULL,
    State TEXT NOT NULL,
    Country TEXT NOT NULL,
    LastUpdate DATE NOT NULL,
    Confirmed INTEGER NOT NULL,
    Deaths INTEGER NOT NULL,
    Recovered INTEGER NOT NULL);
'''

cursor.execute(create_table)

file = open('/home/prudhvi/covid_19/db/covid_clean_data.csv')

contents = csv.reader(file)

insert_records = "INSERT INTO covid (ObservationDate,State,Country,LastUpdate,Confirmed,Deaths,Recovered) VALUES (?,?,?,?,?,?,?)"

cursor.executemany(insert_records, contents)

print_stmt = 'SELECT * FROM covid'

rows = cursor.execute(print_stmt).fetchall()

for r in rows:
    print(r)

connection.commit()

connection.close()