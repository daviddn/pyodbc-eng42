# Connecting SQL to Python using pyodbc

This is an example of us connecting to our SQL server, using python and pyodbc.

We will look into:
- Cursor
- Rows
- Querying the db
- Using While loops for efficient data queries
- Transactions

## connection
Establishing a connection with a database.

## .cursor()
Allows us to execute read only queries on the database.

## cursor().execute()
Executes desired SQL argument.

## .fetchall() vs .fetchone()
Fetch rows from cursor, or just one.