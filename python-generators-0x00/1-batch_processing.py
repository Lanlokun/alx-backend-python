import sqlite3

def stream_users_in_batches(batch_size):
    """
    Generator function that fetches rows from the users table in batches.

    Args:
        batch_size (int): The size of each batch.
    
    Yields:
        list: A batch of rows from the users table.
    """
    connection = sqlite3.connect('alxprodev.db')  # Replace with your database path
    try:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM users")
        
        while True:
            batch = cursor.fetchmany(batch_size)
            if not batch:
                break
            yield batch
    finally:
        connection.close()

def batch_processing(batch_size):
    """
    Processes each batch of users to filter those over the age of 25.

    Args:
        batch_size (int): The size of each batch.

    Yields:
        list: A filtered batch of users over the age of 25.
    """
    for batch in stream_users_in_batches(batch_size):
        filtered_users = [user for user in batch if user[2] > 25]
        yield filtered_users