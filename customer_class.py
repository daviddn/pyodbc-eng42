from oop_db_connect import *

class Customer(ConnectMsS):

    def list_all_sql_entries(self):
        query = self.filter_query(f"SELECT * FROM Customers")
        while True:
            record = query.fetchone()
            if record is None:
                break
            print(record)

    def read_one_sq_id(self, number):
        query = self.filter_query(f"SELECT * FROM Customers WHERE CustomerID = {number}").fetchone()
        return query