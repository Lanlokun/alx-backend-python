import sqlite3

# Decorator to log database queries
def log_queries(func):
    """
    A decorator to log the SQL query executed by the function.
    """
    def wrapper(*args, **kwargs):
        cursor = args[0]  # This assumes the first argument is always the cursor
        
        sql_query = kwargs.get('query') if 'query' in kwargs else args[1] if len(args) > 1 else None
        
        if sql_query:
            print(f"Executing SQL Query: {sql_query}") 
            
        return func(*args, **kwargs)
    
    return wrapper

# Example function using the decorator to interact with a database
@log_queries
def execute_query(cursor, query):
    """
    Executes a given SQL query using the provided cursor.
    """
    cursor.execute(query)
    return cursor.fetchall()
