import pyodbc

# In this file we'll make our connection

# Parameters/variables for connetion
server = 'localhost, 1433'
database = 'Northwind'
username = 'SA'
password = 'Passw0rd2018'

# Establish a connection
conn_nwdb = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+password)

print(conn_nwdb)
# Create a cursor
# Allows us to execute read only queries on the db
cursor = conn_nwdb.cursor()

# Using .execute() on cursor
cursor.execute("SELECT * FROM Customers;")

# Fetch rows from cursor - .fetchone()
row = cursor.fetchone()
# print(row)

row = cursor.fetchone()
print(row.ContactName) # it maintains state

row = cursor.fetchone()
print(row.ContactName) # it maintains state

# Fetch all - .fetchall()
# This is bad MM'kay?
# We don't this mm'kay..
rows = cursor.execute("SELECT * FROM Customers").fetchall()
# print(rows)
print(len(rows))
print(type(rows)) # If this is a list, then:

rows = cursor.execute("SELECT * FROM Products").fetchall()
# We can iterate
for record in rows:
    print(type(record))
    print(record.UnitPrice) # We can access the column of a specific record

# This is bad MM'kay?
# We don't this mm'kay..

# However, this is dangerous as we said.
# Because we can clog our machine with too much data
    # We can use While loop to be more efficient

rows = cursor.execute("SELECT * FROM Products")

while True:
    record = rows.fetchone()
    if record is None:
        break
    print(record.UnitPrice)