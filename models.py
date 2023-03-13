import sqlite3
from flask import g
DATABASE_FILE = 'bookshop.db'
#db = SQLAlchemy()

def get_db_connection():
    conn = sqlite3.connect(DATABASE_FILE)
    return conn
#db = get_db_connection()
db = sqlite3.connect(DATABASE_FILE)

cursor = db.cursor()
query = f"""CREATE TABLE IF NOT EXISTS User (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  firstname TEXT NOT NULL,
  username TEXT NOT NULL UNIQUE,
  email TEXT NOT NULL UNIQUE,
  password TEXT NOT NULL
);"""

query2 = f"""CREATE TABLE IF NOT EXISTS Books (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  title TEXT NOT NULL,
  author TEXT NOT NULL,
  date TEXT NOT NULL,
  user_id INTEGER NOT NULL
);"""
cursor.execute(query)
cursor.execute(query2)
