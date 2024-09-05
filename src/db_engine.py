"""
Database file to connect, execute commands and close connection
"""

import os
from dotenv import load_dotenv
import psycopg2
import pandas as pd

load_dotenv()
class DBEngine:
    def __init__(self):
        self.connection = self.connect()
        self.cursor = self.connection.cursor()

    @staticmethod
    def connect():
        """
        Prisijungiam prie duomenu bazes pagal info env faile
        :return: connection duomenu bazes objektas
        """
        try:
            connection = psycopg2.connect(
                dbname=os.getenv('DATABASE_NAME'),
                user=os.getenv('DB_USERNAME'),
                password=os.getenv('PASSWORD'),
                host=os.getenv('HOST'),
                port=os.getenv('PORT')
            )
            print("PostgreSQL connection is opened")
            return connection
        except (Exception, psycopg2.Error) as error:
            print("Error while connecting to PostgreSQL", error)
            return None

    def execute_sql(self, query, params=None):
        """
        Paleidziam komanda SQL.
        :param query: Komanda kuria norime paleist
        :param params: Opcionalus parametrai
        :return: Komandos rezultatas: tuple
        """
        try:
            self.cursor.execute(query, params)
            self.connection.commit()
            return self.cursor.fetchall()
        except (Exception, psycopg2.Error) as error:
            print("Error while executing query", error)
            self.connection.rollback()
            return None

    def disconnect(self):
        """
        Uždaro duomenų bazės ryšį
        :return None
        """
        try:
            if self.cursor:
                self.cursor.close()
            if self.connection:
                self.connection.close()
                print('PostgreSQL connection is closed')
        except (Exception, psycopg2.Error) as error:
            print("Error while closing PostgreSQL connection", error)

    def __del__(self):
        self.disconnect()

if __name__ == "__main__":
    db = DBEngine()
    if db.connection:
        result = db.execute_sql(
            ""
) # Example query
        print(f"{result}")
        print(f"Command executed")