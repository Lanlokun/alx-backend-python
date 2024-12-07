import sqlite3
from datetime import datetime

def log_queries(func):
    """
    A decorator to log the SQL query executed by the function, along with the timestamp.
    """
    def wrapper(*args, **kwargs):
        cursor = args[0] 
        
        sql_query = kwargs.get('query') if 'query' in kwargs else args[1] if len(args) > 1 else None
        
        if sql_query:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            print(f"[{timestamp}] Executing SQL Query: {sql_query}")
        
        return func(*args, **kwargs)
    
    return wrapper

@log_queries
def execute_query(cursor, query):
    """
    Executes a given SQL query using the provided cursor.
    """
    cursor.execute(query)
    return cursor.fetchall()