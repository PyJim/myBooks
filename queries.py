from flask import g
import sqlite3

def get_db_connection():
    conn = sqlite3.connect('bookshop.db')
    return conn


def db_query(query, Args=()):
    conn = get_db_connection()
    res = conn.execute(query, Args)
    rv = res.fetchall()
    conn.close()
    return rv

def db_execute(script, Args=()):
    conn = get_db_connection()
    conn.execute(script, Args)
    conn.commit()
    conn.close()
    return True

def create_user(firstname, username, email, password):
    query = """INSERT INTO user (firstname, username, email, password) VALUES (?, ?, ?, ?);"""
    return db_execute(query, [firstname, username, email, password])
    
def check_user(email, username):
    query1 = f"""SELECT * FROM User WHERE email=?;"""
    query2 = f"""SELECT * FROM User WHERE username=?;"""

    email_check = db_query(query1, [email])
    username_check = db_query(query2, [username])
    return [email_check, username_check]

def find_user(username):
    query = 'SELECT * FROM User WHERE username=?;'
    return db_query(query, [username])

class PasswordCheck:
    def __init__(self, password1, password2):
        self.password1 = password1
        self.password2 = password2
    
    def mismatch(self):
        return self.password1 != self.password2
    
    def not_strong(self):
        return len(self.password1)<6

class EmailCheck:
    def __init__(self, email):
        self.email = email
    
    def invalid(self):
        return "@" not in self.email

def signup_empty(username, email, password, firstname):
    first = firstname == ''
    user = username == ''
    email = email == ''
    pwd = password == ''

    return first or user or email or pwd

def signin_empty(username, password):
    user = username == ''
    pwd = password == ''
    return user or pwd


# working on the books
def get_user_books(user_id):
    query = """SELECT * FROM Books WHERE user_id =?;"""
    return db_query(query, [user_id])

def add_user_book(title, author, user_id, date):
    query = """INSERT INTO Books (title, author, user_id, date) VALUES (?, ?, ?, ?);"""
    return db_execute(query, [title, author, user_id, date])

#searching for book

def deleteBook(user_id, title, author):
    query = """DELETE FROM Books WHERE user_id=? AND title=? AND author=?;"""
    db_execute(query, [user_id, title, author])
    


def change_book_details(title, author, user_id):
    query = """UPDATE Books SET title = ?, author = ? WHERE user_id = ?;"""
    db_execute(query, [title, author, user_id])

# editing details

def change_user_details(firstname, password, id):
    query = """UPDATE User SET firstname = ?, password = ? WHERE id = ?;"""
    db_execute(query, [firstname, password, id])
