'''
This module demonstrates the Expression Language of SQLAlchemy.

Installed with:
`pip3 install sqlalchemy==1.4.46`
'''


from sqlalchemy import (
    create_engine, Table, Column, Float, ForeignKey, Integer, String, MetaData
)


# Link our Python file to the chinook database, using create_engine:
# The triple forward slashes represent that the database is hosted in
# our local environment.
db = create_engine("postgresql:///chinook")

# Create our metadata - data about data of our table objects:
meta = MetaData(db)

# Construct the tables so that Python knows the schema/data models we
# are working with:
# Using the imported 'Table' class, we supply the table name and meta
# schema.

# TIP FOR SEEING LIST OF COLUMN HEADERS ON A TABLE IN SQL CLI:
# `SELECT * FROM "Table" WHERE false;`
# Use this information for the following construction of tables.

# Within the Table class argument, define the columns in this format:
# (Name, Type, Optional Fields)
# The 'Column' import is utilized here.

# TABLE DEFINITIONS ----------------------------------------------------

# Variable for the "Artist" table:
artist_table = Table(
    "Artist", meta,
    Column("ArtistId", Integer, primary_key=True),
    Column("Name", String)
)

# Variable for the "Album" table:
album_table = Table(
    "Album", meta,
    Column("AlbumId", Integer, primary_key=True),
    Column("Title", String),
    # Point to the correct table and key to define the foreign key:
    Column("ArtistId", Integer, ForeignKey("artist_table.ArtistId"))
)

# Variable for the "Track" table:
track_table = Table(
    "Track", meta,
    Column("TrackId", Integer, primary_key=True),
    Column("Name", String),
    Column("AlbumId", Integer, ForeignKey("album_table.AlbumId")),
    # Technically a foreign key, but as we are only defining the tables we
    # need and not all, PK is set to False:
    Column("MediaTypeId", Integer, primary_key=False),
    Column("GenreId", Integer, primary_key=False),
    Column("Composer", String),
    Column("Milliseconds", Integer),
    Column("Bytes", Integer),
    # Unit price uses decimals, hence float type.
    Column("UnitPrice", Float)
)

# Make the actual connection to the database:
# Use the connect() method to save the connection into a variable called
# 'connection'.
with db.connect() as connection:
    # START QUERIES AFTER TABLE DEFINITIONS ------------------------------

    # Define all six queries into variable 'select_query, using expression
    # language:

    # Q1 All records from "Artist" table
    # select_query = artist_table.select()

    # Q2 "Name" col from "Artist" table
    # The .with_only_columns() method must be supplied a list, no matter
    # how many columns we are searching for.
    # We use the dot notation with 'c' to specify the column required.
    # select_query = artist_table.select().with_only_columns([
    # artist_table.c.Name])

    # Q3 'Queen' from "Artist"
    # Use the .where() method with similar notation as Q2
    # select_query = artist_table.select().where(
    # artist_table.c.Name == "Queen")

    # Q4 ArtistId == 51 from "Artist"
    # select_query = artist_table.select().where(artist_table.c.ArtistId == 51)

    # Q5 Albums with ArtistId == 51 from "Album" table
    # select_query = album_table.select().where(album_table.c.ArtistId == 51)

    # Q6 attempt: show tracks by Queen
    # This is based off the raw SQL query RESULTS shown in the lesson
    # video
    select_query = track_table.select().where(
        track_table.c.Composer == "Queen")

    # ^ CORRECT! Remember that the 'c' must still be included to specify
    # the column whose attribute we are looking for.

    # Run the query using the execute() method from the database
    # connection. The queries are stores in variable 'results' so that
    # they may be iterated over.
    results = connection.execute(select_query)
    for result in results:
        print(result)
