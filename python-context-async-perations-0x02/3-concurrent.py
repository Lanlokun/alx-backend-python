import sqlite3
import aiosqlite
import asyncio

class ExecuteQuery:
    def __init__(self, query, parameters):
        self.query = query
        self.parameters = parameters
        self.connection = None
        self.cursor = None

    def __enter__(self):
        """Establish the database connection and prepare the cursor."""
        # Establish a connection to the database
        self.connection = sqlite3.connect("example.db")  # Replace with your database path
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
        # Handle exceptions (if any occurred) by returning False to propagate them
        return False

# Asynchronous functions for concurrent queries
async def async_fetch_users():
    query = "SELECT * FROM users"
    async with aiosqlite.connect("example.db") as db:
        async with db.execute(query) as cursor:
            return await cursor.fetchall()

async def async_fetch_older_users():
    query = "SELECT * FROM users WHERE age > 40"
    async with aiosqlite.connect("example.db") as db:
        async with db.execute(query) as cursor:
            return await cursor.fetchall()

async def fetch_concurrently():
    results = await asyncio.gather(
        async_fetch_users(),
        async_fetch_older_users()
    )
    print("All Users:", results[0])
    print("Users Older Than 40:", results[1])

# Example usage
if __name__ == "__main__":
    asyncio.run(fetch_concurrently())
