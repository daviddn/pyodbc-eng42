from oop_db_connect import *
from product_class import *
from customer_class import *

# db_nw = ConnectMsS()
# print(db_nw)
# print(db_nw.conn_nwdb)
#
# print(db_nw.cursor.execute("SELECT * FROM Products").fetchone().UnitPrice)
#
# print(db_nw.sql_query_fetchone("SELECT * FROM Products"))
#
# print(db_nw.return_avg_unit_price_products())

products_nw = Product()
customers_nw = Customer()
# products_nw.list_all_sql_entries()

# print(products_nw.read_one_sq_id("5"))
print(customers_nw.read_one_sq_id("'ALFKI'"))