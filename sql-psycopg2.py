'''
This module demonstrates the use of psycopg2, which allows for SQL
queries to be made in Python.

Installed with:
`pip3 install psycopg2`
'''


# psycopg2 Python data adapter for Postgres
import psycopg2


# Connect to 'chinook' database
connection = psycopg2.connect(database="chinook")


# Build a cursor object (similar to a list)
cursor = connection.cursor()


# PERFORM QUERIES HERE BELOW CURSOR DEFINITION

# Query 1 - select all records from the "Artist" table
# PyscoPG2 commands are similar native SQL commands.
# Note that queries MUST be wrapped in single quotation marks.
# cursor.execute('SELECT * FROM "Artist"')

# Q2
# cursor.execute('SELECT "Name" FROM "Artist"')

# Q3
# Note the use of Python string placeholder/list technique, due to the
# quotation marks limitations in psycopg2.
# cursor.execute('SELECT * FROM "Artist" WHERE "Name" = %s', ["Queen"])

# Q4
# cursor.execute('SELECT * FROM "Artist" WHERE "ArtistId" = 51')
# OR:
# cursor.execute('SELECT * FROM "Artist" WHERE "ArtistId" = %s', [51])

# Q5
# cursor.execute('SELECT * FROM "Album" WHERE "ArtistId" = 51')

# Q6
# cursor.execute('SELECT * FROM "Track" WHERE "Composer" = %s', ["Queen"])

# OWN TEST QUERIES:

# Q7
cursor.execute('SELECT * FROM "Track" WHERE "Composer" = %s', ["Metallica"])

# Q8
# cursor.execute('SELECT * FROM "Track" WHERE "Composer" = %s', ["test"])


# Before querying the database, set up a way to fetch data from the
# cursor
# Multiple results:
results = cursor.fetchall()
# Single results:
# Single results are printed line-by-line, instead of as tuples.
# results = cursor.fetchone()


# Close the connection after results have been fetched
connection.close()


# Retrieve each result from the cursor object and print
for result in results:
    print(result)
