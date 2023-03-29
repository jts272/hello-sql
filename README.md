# Database Management Systems - PostgreSQL and Python

Note - enter `set_pg` in the terminal prior to using the `psql` command.

The CI Gitpod full template is used in this repo.

Postres is the open-source RDBMS used (object-relational).

The pre-existing "Chinook" database is used to demonstrate the use of the
database queries herein. See the `Chinook-PostgreSql.sql` file.

From here, we enter the Postgres CLI with `psql` and create a new database with
SQL commands (remember the semicolon!).

Commands can be used to save results to `.csv` or `.json`.

## Database adapters

PsycoPG2 - see `sql-psycopg2.py` comments

ORM - Object-relational mapper - see `sql-expression.py` comments for expression
syntax

## CRUD

CRUD functionality can be found in `sql-crud.py`.

Querying the chinook database with `\dt` will show the new 'Programmer' table
added from the crud session.

Confirm the new entry(s) with `SELECT * FROM "Programmer";`