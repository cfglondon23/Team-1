import sqlite3

# Create a connection to the database
conn = sqlite3.connect('education.db')

# Create a cursor object to execute SQL commands
c = conn.cursor()

# Create a table with two columns: id and name
c.execute('''CREATE TABLE IF NOT EXISTS example_table
             (id INTEGER PRIMARY KEY, name TEXT)''')

# Insert some data into the table
c.execute("INSERT INTO example_table (name) VALUES ('Alice')")
c.execute("INSERT INTO example_table (name) VALUES ('Bob')")

# Commit the changes to the database
conn.commit()

# Close the connection
conn.close()
