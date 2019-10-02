from connect_nwdb import *

query = cursor.execute("SELECT COUNT(*) FROM Orders WHERE ShipCity = 'Rio de Janeiro'").fetchone()[0]

print(query)