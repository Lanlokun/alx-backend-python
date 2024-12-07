import sqlite3
import functools
from datetime import datetime

# Decorator to log SQL queries
def log_queries(func):
    """
    A decorator to log the SQL query executed by the function, along with the timestamp.
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        query = kwargs.get('query') if 'query' in kwargs else args[0]
        
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"[{timestamp}] Executing SQL Query: {query}")
        
        return func(*args, **kwargs)
    
    return wrapper

@log_queries
def fetch_all_users(query):
    """
    Executes a given SQL query to fetch all users.
    """
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    conn.close()
    return results

users = fetch_all_users(query="SELECT * FROM users")

print(users)
