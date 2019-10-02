import pyodbc

# Concept of 'Strong Params'
    # Never EVER, Trust user input
    # Avoid SQL injections
    # Filter for SQL injections

class ConnectMsS():

    def __init__(self, server = 'localhost, 1433', database = 'Northwind', username = 'SA', password = 'Passw0rd2018'):
        self.server = server
        self.database = database
        self.username = username
        self.password = password
        self.conn_nwdb = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+self.server+';DATABASE='+self.database+';UID='+self.username+';PWD='+self.password)
        self.cursor = self.conn_nwdb.cursor()

    def filter_query(self, query): # Strong params/Filter
        # Doing some filtering for bad queries
        return self.cursor.execute(query)

    def sql_query(self, query):
        return self.filter_query(query)

    def sql_query_fetchone(self, query):
        return self.filter_query(query).fetchone()

    def print_all_product_records_from_table(self):
        query_rows = self.filter_query(f"SELECT * FROM Products")
        while True:
            record = query_rows.fetchone()
            if record is None:
                break
            print(record)

    # def print_average_product_price(self):
    #     query_rows = self.__filter_query("SELECT AVG(UnitPrice) FROM Products")
    #     while True:
    #         record = query_rows.fetchone()
    #         if record is None:
    #             break
    #         print(record)

    def return_avg_unit_price_products(self):
        # Query
        query = self.filter_query("SELECT * FROM Products")
        # Sum all the unit prices
        prices = []

        while True:
            # get individual prices and append to my list
            record = query.fetchone()
            if record is None:
                break
            prices.append(record.UnitPrice)
        # Sum all unite prices
        # Divide by length of rows
        return (sum(prices)/len(prices))

    # CRUD

    # Create 1 entry
        # use INSERT
        # the Cursor cannot make transactions (go to documentation)

    # Read all entries
        # fetch all records and return as a List of Dictionaries
    # def list_all_sql_entries(self, table):
    #     query = self.__filter_query(f"SELECT * FROM {table}")
    #     while True:
    #         record = query.fecthone()
    #         if record is None:
    #             break
    #         print(record)
    # # Read one entry
    #     # fetch a specific record
    #     # get one value using ID
    # def read_one_sq_id(self, table, id, number):
    #     query = self.__filter_query(f"SELECT * FROM {table} WHERE {id} = {number}").fetchone()
    #     return query

    # Update 1 entry
        # the ID of the record to update
        # update the specific record
        # use UPDATE TABLE
        # the Cursor cannot make transactions

    # Destroy / one entry
        # the ID of the specific record
        # destroy the record
        # the Cursor cannot make transactions