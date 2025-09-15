#API (Application Programming Interface): A way for programs to communicate with each other.

#In Python, the requests library is used for HTTP APIs.
import requests

response = requests.get("https://api.github.com")
if response.status_code == 200:
    print("API Response:", response.json())
else:
    print("Error:", response.status_code)

 #(b)Connect to sqLite Database
    import sqlite3

# 1. Connect to (or create) a database
    connection = sqlite3.connect("example.db")

 # 2. Create a cursor object
    cursor = connection.cursor()

 # 3. Create a table
    cursor.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT)")

# 4. Insert data
    cursor.execute("INSERT INTO users (name) VALUES (?)", ("Alice",))

 # 5. Commit changes
    connection.commit()

 # 6. Query data
    cursor.execute("SELECT * FROM users")
    print("Users:", cursor.fetchall())

 # 7. Close connection
    connection.close()

#  Steps
#explained:
#1.Connect → Creates or opens the database file.
# 2.Cursor → Used to execute SQL commands.
# 3.Create table → Defines structure of stored data.
# 4.Insert → Adds records.
 # 5.Commit → Saves changes.
# 6.Select → Reads stored data.
#7.Close → Closes the database safely.