# SETUP COPIED FROM sql-orm.py
# Includes imports, variables and Session/metadata.
# Float and ForeignKey not required.

# Table and MetaData Classes not needed - we are creating Python
# classes, not tables.
from sqlalchemy import (create_engine, Column, Integer, String)

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


# CREATION OF CLASS-BASED MODELS (Table Schema) ------------------------
# Based on some of the greatest programmers of all time.

class Programmer(base):
    __tablename__ = "Programmer"
    # PK auto-increments with each new record added.
    # e.g. first record assigned id of 1, second = 2 etc.
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    gender = Column(String)
    nationality = Column(String)
    famous_for = Column(String)


# SESSION VARIABLES ----------------------------------------------------

# Create a new instance of sessionmaker and point to our engine(db).
# This instantiates the sessionmaker() class from the ORM.
Session = sessionmaker(db)

# Open the ACTUAL session by calling the Session() subclass defined
# above,
session = Session()

# Create the database subclass and generate all metadata. This is
# subclassed from the declarative_base.
base.metadata.create_all(db)


# CRUD CREATE ----------------------------------------------------------

ada_lovelace = Programmer(
    first_name="Ada",
    last_name="Lovelace",
    gender="F",
    nationality="English",
    famous_for="First Programmer"
)

alan_turing = Programmer(
    first_name="Alan",
    last_name="Turing",
    gender="M",
    nationality="English",
    famous_for="Modern Computing"
)

grace_hopper = Programmer(
    first_name="Grace",
    last_name="Hopper",
    gender="F",
    nationality="American",
    famous_for="COBOL Language"
)

margaret_hamilton = Programmer(
    first_name="Margaret",
    last_name="Hamilton",
    gender="F",
    nationality="American",
    famous_for="Apollo 11"
)

bill_gates = Programmer(
    first_name="Bill",
    last_name="Gates",
    gender="M",
    nationality="American",
    famous_for="Microsoft"
)

tim_berners_lee = Programmer(
    first_name="Tim",
    last_name="Berners-Lee",
    gender="M",
    nationality="English",
    famous_for="World Wide Web"
)

# Custom entry
joe_smith = Programmer(
    first_name="Joe",
    last_name="Smith",
    gender="M",
    nationality="English",
    famous_for="Meme"
)

# # Add the instances of each programmer to our session
# session.add(ada_lovelace)
# # ^ COMMENT OUT AFTER ADDING TO PREVENT REPEAT ENTRY TO TABLE!
# session.add(alan_turing)
# session.add(grace_hopper)
# session.add(margaret_hamilton)
# session.add(bill_gates)
# session.add(tim_berners_lee)
# session.add(joe_smith)


# CRUD UPDATE ----------------------------------------------------------

# # FOR SINGLE RECORD
# # Use PK to find, as this is unique (Programmers may share first names).
# # GET VAR
# programmer = session.query(Programmer).filter_by(id=17).first()
# # SET VAR (Whichever columns need updating)
# programmer.famous_for = "World President"

# # Commit the session to the database
# # session.commit()


# # FOR MULTIPLE RECORDS
# # Use new var 'people' as 'programmers' is already in use for printing
# people = session.query(Programmer)
# # Loop to update all records at once
# for person in people:
#     if person.gender == "F":
#         person.gender = "Female"
#     elif person.gender == "M":
#         person.gender = "Male"
#     else:
#         print("Gender not defined")

#     # Commit the updates WITHIN the loop
#     session.commit()


# CRUD DELETE ----------------------------------------------------------
# Users probably won't have access to any PKs.
# We can use input fields to prompt the user to find an entry

# # FOR SINGLE RECORD
# fname = input("Enter a first name: ")
# lname = input("Enter a last name: ")
# # Just plug these vars into the filter
# programmer = session.query(Programmer).filter_by(
#     first_name=fname, last_name=lname).first()

# # Defensive programming
# if programmer is not None:
#     print(
#         "Programmer found: ", programmer.first_name + " " +
#         programmer.last_name)
#     # var to check for confirmation of deletion
#     confirmation = input(
#         "Are you sure you want to delete this record? (Y/N)"
#     )
#     if confirmation.lower() == "y":
#         session.delete(programmer)
#         # Commit the change
#         session.commit()
#         print("Programmer has been deleted")
#     else:
#         print("Programmer not deleted")
# else:
#     print("No records found")


# # FOR ALL RECORDS
# # Use defensive programming in a real world scenario. Get input and
# # confirmation.
# programmers = session.query(Programmer)
# for programmer in programmers:
#     session.delete(programmer)
#     session.commit()
# print("All records deleted!")

# NOTE THAT THIS DOES NOT RESET THE PRIMARY KEYS


# CRUD READ ------------------------------------------------------------

programmers = session.query(Programmer)
for programmer in programmers:
    print(
        programmer.id,
        programmer.first_name + " " + programmer.last_name,
        programmer.gender,
        programmer.nationality,
        programmer.famous_for,
        sep=" | "
    )
