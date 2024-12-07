import sqlite3

def stream_user_ages():
    """
    A generator that streams user ages from the database one by one.

    Yields:
        int: The age of a user.
    """
    connection = sqlite3.connect('database.db')
    try:
        cursor = connection.cursor()
        query = "SELECT age FROM user_data" 
        cursor.execute(query)

        while True:
            row = cursor.fetchone()
            if row is None:
                break  
            yield row[0] 
    finally:
        connection.close()

def calculate_average_age():
    """
    Calculates the average age of users using the stream_user_ages generator.
    
    Prints the average age.
    """
    total_age = 0
    count = 0
    
    # Using the generator to get user ages one by one
    for age in stream_user_ages():
        total_age += age 
        count += 1  
    
    if count > 0:
        average_age = total_age / count 
        print(f"Average age of users: {average_age:.2f}")
    else:
        print("No users found.")

# Call the function to calculate and print the average age
calculate_average_age()
