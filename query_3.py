from connect_nwdb import *

query = cursor.execute("SELECT COUNT(*) FROM Orders WHERE ShipCity = 'Rio de Janeiro' OR ShipCity = 'Reims'").fetchone()[0]

print(query)