import time
import sqlite3
import functools

# Cache dictionary to store query results
query_cache = {}

def with_db_connection(func):
    """
    Decorator to automatically handle opening and closing the database connection.
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        conn = sqlite3.connect('database.db')
        
        try:
            return func(conn, *args, **kwargs)
        finally:
            conn.close()
    
    return wrapper

def cache_query(func):
    """
    Decorator that caches the result of a query based on the SQL query string.
    """
    @functools.wraps(func)
    def wrapper(conn, query, *args, **kwargs):
        if query in query_cache:
            print("Fetching from cache...")
            return query_cache[query]
        
        result = func(conn, query, *args, **kwargs)
        
        query_cache[query] = result
        return result
    
    return wrapper

@with_db_connection
@cache_query
def fetch_users_with_cache(conn, query):
    """
    Fetch users from the database, caching the results to avoid redundant calls.
    """
    cursor = conn.cursor()
    cursor.execute(query)
    return cursor.fetchall()

# First call will cache the result
users = fetch_users_with_cache(query="SELECT * FROM users")
print(users)

# Second call will use the cached result
users_again = fetch_users_with_cache(query="SELECT * FROM users")
print(users_again)
