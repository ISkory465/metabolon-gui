import psycopg2
from configparser import ConfigParser
from .db_config import configDB

class DatabaseHandler:
    def __init__(self):
        self.connection = None
        self.params = configDB()
        self.cursor = None
        
        try:
            print('Connecting to database')
            self.connection = psycopg2.connect(**self.params)
            
            # Create cursor
            self.cursor = self.connection.cursor()
            print('Database version:')
            self.cursor.execute('SELECT version()')
            db_version = self.cursor.fetchone()
            print(db_version)
            self.cursor.close()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)

    def insert_record(self, table_name, column_name, value):
        self.cursor = self.connection.cursor()
        insert_query = f"INSERT INTO {table_name} ({column_name}) VALUES (%s);"
        self.cursor.execute(insert_query, (value,))
        self.connection.commit()
        self.cursor.close()


    def update_record(self, table_name, column_name, new_value, condition):
        self.cursor = self.connection.cursor()
        update_query = f"UPDATE {table_name} SET {column_name} = %s WHERE {condition};"
        self.cursor.execute(update_query, (new_value,))
        self.connection.commit()
        self.cursor.close()

    def get_records(self, table_name):
        self.cursor = self.connection.cursor()
        select_query = f"SELECT * FROM {table_name};"
        self.cursor.execute(select_query)
        records = self.cursor.fetchall()
        self.cursor.close()
        return records
    
    def close_connection(self):
        if self.cursor is not None:
            self.cursor.close()
        if self.connection is not None:
            self.connection.close()
            print('Database connection closed')
        
        
if __name__ == "__main__":
    db_handler = DatabaseHandler()
    db_handler.update_record('opcdb78', 'he11_bh', '10')
    