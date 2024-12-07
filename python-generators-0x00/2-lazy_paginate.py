import sqlite3

def paginate_users(page_size, offset):
    """
    Fetches a page of users from the database.

    Args:
        page_size (int): The number of users to fetch per page.
        offset (int): The offset for the pagination query (i.e., how many users to skip).
    
    Yields:
        list: A batch of users for the current page.
    """
    connection = sqlite3.connect('database.db')
    try:
        cursor = connection.cursor()
        query = f"SELECT * FROM user_data LIMIT {page_size} OFFSET {offset}"
        cursor.execute(query)
        
        batch = cursor.fetchall()
        if batch:
            yield batch
    finally:
        connection.close()

def lazy_paginate(page_size):
    """
    Lazily fetches users in pages from the database.

    Args:
        page_size (int): The number of users per page.
    
    Yields:
        list: A batch of users, one page at a time.
    """
    offset = 0
    while True:
        users_batch = paginate_users(page_size, offset)
        
        batch = next(users_batch, None)
        
        if batch:
            yield batch
            offset += page_size
        else:
            break
