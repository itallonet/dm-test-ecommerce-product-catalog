import psycopg2
from psycopg2.extras import RealDictCursor
import os

def get_db():
    try:
        conn = psycopg2.connect(
            dbname="productdb",
            user="user",
            password="password",
            host="db",
            port="5432"
        )
        return conn
    except Exception as e:
        print("Database connection failed due to {}".format(e))

def get_db_cursor(conn):
    return conn.cursor(cursor_factory=RealDictCursor)
