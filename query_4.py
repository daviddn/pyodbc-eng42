from connect_nwdb import *

query = cursor.execute("SELECT * FROM Customers WHERE CompanyName LIKE '%z%' OR CompanyName LIKE '%Z%'").fetchall()

print(query)