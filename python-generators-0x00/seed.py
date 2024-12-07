import mysql.connector
import csv
import uuid

# Function to connect to MySQL database server
def connect_db():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",  
            password="" 
        )
        print("Connected to MySQL server.")
        return connection
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None

# Function to create the ALX_prodev database if it does not exist
def create_database(connection):
    cursor = connection.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS ALX_prodev")
    print("Database ALX_prodev created or already exists.")
    cursor.close()

# Function to connect to the ALX_prodev database
def connect_to_prodev():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="ALX_prodev"
        )
        print("Connected to ALX_prodev database.")
        return connection
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None

# Function to create the user_data table if it does not exist
def create_table(connection):
    cursor = connection.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS user_data (
            user_id CHAR(36) PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            email VARCHAR(255) NOT NULL,
            age DECIMAL(3, 0) NOT NULL,
            INDEX (user_id)
        )
    """)
    print("Table user_data created or already exists.")
    cursor.close()

# Function to insert data into the database if it does not exist
def insert_data(connection, data):
    cursor = connection.cursor()
    cursor.execute("SELECT user_id FROM user_data WHERE email = %s", (data['email'],))
    if cursor.fetchone() is None:  # Check if the data already exists
        cursor.execute("""
            INSERT INTO user_data (user_id, name, email, age)
            VALUES (%s, %s, %s, %s)
        """, (data['user_id'], data['name'], data['email'], data['age']))
        connection.commit()
        print(f"Inserted data: {data}")
    else:
        print(f"Data already exists for email: {data['email']}")
    cursor.close()