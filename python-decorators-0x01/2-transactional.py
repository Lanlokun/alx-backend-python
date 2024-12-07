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

def transactional(func):
    """
    Decorator that wraps the function in a database transaction.
    Commits the transaction if successful, rolls back if there's an error.
    """
    @functools.wraps(func)
    def wrapper(conn, *args, **kwargs):
        try:
            # Start a transaction
            result = func(conn, *args, **kwargs)
            conn.commit()
            return result
        except Exception as e:
            # Rollback in case of error
            conn.rollback()
            print(f"Error occurred: {e}")
            raise 
    return wrapper

@with_db_connection
@transactional
def update_user_email(conn, user_id, new_email):
    """
    Updates the email of a user by their user_id.
    """
    cursor = conn.cursor()
    cursor.execute("UPDATE users SET email = ? WHERE id = ?", (new_email, user_id))

# Update user's email with automatic transaction handling
update_user_email(user_id=1, new_email='Kim_Willms@hotmail.com')
