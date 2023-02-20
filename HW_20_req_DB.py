import sqlite3

connection = sqlite3.connect("education.sqlite")
# print(connection)

cursor = connection.cursor()
data = [
    ("Andrii", "Yershov", 25),
    ("Andrii", "Yershov", 26),
    ("Andrii", "Yershov", 27),
    ("Andrii", "Yershov", 28),
    ("Andrii", "Yershov", 29),
]
query = 'INSERT INTO users (first_name, last_name, age) values (?, ?, ?)'

cursor.executemany(query, data)
connection.commit()
