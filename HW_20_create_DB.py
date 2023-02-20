import sqlite3

connection = sqlite3.connect("education.sqlite")
# print(connection)

cursor = connection.cursor()

query = ('CREATE TABLE IF NOT EXISTS users ('
         'id INTEGER PRIMARY KEY AUTOINCREMENT,'
         'first_name TEXT,'
         'last_name TEXT,'
         'age INTEGER)')

cursor.execute(query)
connection.commit()
