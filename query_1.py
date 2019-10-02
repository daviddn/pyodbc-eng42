from connect_nwdb import *

query = cursor.execute("SELECT COUNT(*) FROM Orders;").fetchone()[0]

print(query)