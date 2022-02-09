# import sqlite3
# import csv
# import os

# # if os.('covid.db') 

# connection = sqlite3.connect('covid.db')

# cursor = connection.cursor()

# create_table = '''CREATE TABLE covid(
#     SNo INTEGER PRIMARY KEY,
#     ObservationDate DATE NOT NULL,
#     State TEXT NOT NULL,
#     Country TEXT NOT NULL,
#     LastUpdate DATE NOT NULL,
#     Confirmed INTEGER NOT NULL,
#     Deaths INTEGER NOT NULL,
#     Recovered INTEGER NOT NULL);
# '''

# cursor.execute(create_table)

# file = open('/home/prudhvi/covid_19/db/covid_clean_data.csv')

# contents = csv.reader(file)

# insert_records = "INSERT INTO covid (SNo,ObservationDate,State,Country,LastUpdate,Confirmed,Deaths,Recovered) VALUES (?,?,?,?,?,?,?,?)"

# cursor.executemany(insert_records, contents)

# print_stmt = 'SELECT * FROM covid'

# rows = cursor.execute(print_stmt).fetchall()

# for r in rows:
#     print(r)

# connection.commit()

# connection.close()

# #Pandas contain inbuilt method to export as sql table 