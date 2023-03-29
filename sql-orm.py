# Table and MetaData Classes not needed - we are creating Python
# classes, not tables.
from sqlalchemy import (
    create_engine, Column, Float, ForeignKey, Integer, String
)

# Import from SQLAlchemy declarative extension. The Python classes we
# create will subclass the declarative base.
from sqlalchemy.ext.declarative import declarative_base

# sessionmaker required from the ORM. Instead of connecting to the
# database directly, we are asking for a session.
from sqlalchemy.orm import sessionmaker


# Point to our database location
db = create_engine("postgresql:///chinook")

# Get the metadata produced by our database table schema and create a
# subclass to map everything back into this variable.
base = declarative_base()


# CLASS DEFINITIONS (TABLES) -------------------------------------------
# Declared after the base, but before the session.

# Class-based model for the "Artist" table (PascalCase for class names).
class Artist(base):
    __tablename__ = "Artist"
    ArtistId = Column(Integer, primary_key=True)
    Name = Column(String)


# Class-based model for the "Album" table.
# Note again how foreign keys point to the class' column.
class Album(base):
    __tablename__ = "Album"
    AlbumId = Column(Integer, primary_key=True)
    Title = Column(String)
    ArtistId = Column(Integer, ForeignKey("Artist.ArtistId"))


# Class-based model foor the "Track" table.
class Track(base):
    __tablename__ = "Track"
    TrackId = Column(Integer, primary_key=True)
    Name = Column(String)
    AlbumId = Column(Integer, ForeignKey("Album.AlbumId"))
    MediaTypeId = Column(Integer, primary_key=False)
    GenreId = Column(Integer, primary_key=False)
    Composer = Column(String)
    Milliseconds = Column(Integer, primary_key=False)
    Bytes = Column(Integer, primary_key=False)
    UnitPrice = Column(Float)


# Create a new instance of sessionmaker and point to our engine(db).
# This instantiates the sessionmaker() class from the ORM.
Session = sessionmaker(db)

# Open the ACTUAL session by calling the Session() subclass defined
# above,
session = Session()

# Create the database subclass and generate all metadata. This is
# subclassed from the declarative_base.
base.metadata.create_all(db)


# QUERIES --------------------------------------------------------------

# Q1 - All from Artist
# Note use of Python separator
artists = session.query(Artist)
for artist in artists:
    print(artist.ArtistId, artist.Name, sep=" | ")


# Q2 - Name col from Artist
artists = session.query(Artist)
for artist in artists:
    print(artist.Name)

# Q3 - Queen from Artist
# Note our var is singular. No loop as only one instance to be printed.
# We filter and return the first instance, in case of Queen feat etc.
artist = session.query(Artist).filter_by(Name="Queen").first()
print(artist.Name, artist.ArtistId, sep=" | ")

# Q4 - ArtistId 51 from Artist
artist = session.query(Artist).filter_by(ArtistId=51).first()
print(artist.Name, artist.ArtistId, sep=" | ")

# Q5 - Albums where ArtistId = 51
albums = session.query(Album).filter_by(ArtistId=51)
for album in albums:
    print(album.AlbumId, album.Title, Album.ArtistId, sep=" | ")

# Q6 CHALLENGE - Tracks by Queen
tracks = session.query(Track).filter_by(Composer="Queen")
for track in tracks:
    print(
        track.TrackId,
        track.Name,
        track.AlbumId,
        track.MediaTypeId,
        track.GenreId,
        track.Composer,
        track.Milliseconds,
        track.Bytes,
        track.UnitPrice,
        sep=" | ")

# CORRECT! Adjustments made for print arguments formatting.
