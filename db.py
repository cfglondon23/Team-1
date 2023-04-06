import sqlite3
import random
import string

# Create a connection to the database
conn = sqlite3.connect('example.db')

# Create a cursor object to execute SQL commands
c = conn.cursor()

# Define a function to generate a random string of characters
def generate_string(length):
    return ''.join(random.choices(string.ascii_lowercase, k=length))

# Define a function to generate a random integer between 0 and 100
def generate_points():
    return random.randint(0, 100)

# Define a list of locations to choose from
locations = ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix', 'Philadelphia', 'San Antonio', 'San Diego', 'Dallas', 'San Jose']


for i in range(100):
    firstname = generate_string(8)
    lastname = generate_string(10)
    points = generate_points()
    location = random.choice(locations)
    c.execute(f"INSERT INTO volunteers (firstname, lastname, points, location) VALUES ('{firstname}', '{lastname}', {points}, '{location}')")

# Commit the changes to the database
conn.commit()



c.execute("SELECT * FROM volunteers")


# Close the connection
conn.close()
