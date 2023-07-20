import mysql.connector

database = mysql.connector.connect(
    host='localhost',
    user='root',
    password='remya123',
)

cursorobject = database.cursor()

cursorobject.execute('CREATE DATABASE elderco')

print("All done")

