from connect_nwdb import *

query = cursor.execute("SELECT * FROM Orders WHERE ShipCity = 'Rio de Janeiro' OR ShipCity = 'Reims'").fetchall()

print(query)