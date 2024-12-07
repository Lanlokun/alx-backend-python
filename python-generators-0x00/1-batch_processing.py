import sqlite3

def stream_users_in_batches(batch_size, table_name):
    """
    Generator function that fetches rows from the specified table in batches.

    Args:
        batch_size (int): The size of each batch.
        table_name (str): The name of the table to query.
    
    Yields:
        list: A batch of rows from the specified table.
    """
    connection = sqlite3.connect('your_database.db')
    try:
        cursor = connection.cursor()
        query = f"SELECT * FROM user_data"
        cursor.execute(query)
        
        while True:
            batch = cursor.fetchmany(batch_size)
            if not batch:
                break
            yield batch
    finally:
        connection.close()

def batch_processing(batch_size, table_name):
    """
    Processes each batch of rows to filter users over the age of 25.

    Args:
        batch_size (int): The size of each batch.
        table_name (str): The name of the table to query.

    Yields:
        list: A filtered batch of rows over the age of 25.
    """
    for batch in stream_users_in_batches(batch_size, table_name):
        filtered_batch = [user for user in batch if user[2] > 25]
        yield filtered_batch
