import sqlite3
import functools

def with_db_connection(func):
    """
    Decorator that automatically handles opening and closing the database connection.
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # Open a database connection
        conn = sqlite3.connect('database.db')
        try:
            return func(conn, *args, **kwargs)
        finally:
            conn.close()
    
    return wrapper

@with_db_connection
def get_user_by_id(conn, user_id):
    """
    Fetch a user by their ID from the 'users' table.
    """
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))
    return cursor.fetchone()

# Fetch user by ID with automatic connection handling
user = get_user_by_id(user_id=1)
print(user)
