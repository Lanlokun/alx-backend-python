import sqlite3

def stream_users():
    """
    Generator function that streams rows from the user_data table one by one.
    
    Yields:
        tuple: A row from the user_data table.
    """
    # Establish a connection to the database
    connection = sqlite3.connect('your_database.db')
    
    try:
        # Create a cursor object
        cursor = connection.cursor()
        
        # Execute the query to fetch all rows from user_data
        cursor.execute("SELECT * FROM user_data")
        
        # Iterate through the rows and yield one at a time
        for row in cursor:
            yield row
    finally:
        # Ensure the connection is closed
        connection.close()
