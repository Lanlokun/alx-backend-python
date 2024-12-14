import sqlite3

class ExecuteQuery:
    def __init__(self, query, parameters):
        self.query = query
        self.parameters = parameters
        self.connection = None
        self.cursor = None

    def __enter__(self):
        """Establish the database connection and prepare the cursor."""
        self.connection = sqlite3.connect("database.db")
        self.cursor = self.connection.cursor()
        return self

    def execute(self):
        """Execute the provided query with parameters and fetch results."""
        self.cursor.execute(self.query, self.parameters)
        return self.cursor.fetchall()

    def __exit__(self, exc_type, exc_value, traceback):
        """Close the cursor and the connection, handling exceptions if any."""
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()
        return False

query = "SELECT * FROM users WHERE age > ?"
parameters = (25,)

with ExecuteQuery(query, parameters) as executor:
    results = executor.execute()
    print("Query Results:", results)
