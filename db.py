import sqlite3
from faker import Faker
import random

# Create a connection to the database
conn = sqlite3.connect('example.db')

# Create a cursor object to execute SQL commands
c = conn.cursor()

# Create the volunteers table if it doesn't exist
c.execute('''CREATE TABLE IF NOT EXISTS volunteers
             (id INTEGER PRIMARY KEY, firstname TEXT, lastname TEXT, points INTEGER, location TEXT)''')

# Create a Faker instance to generate random names
fake = Faker()

# Define a list of real English city names
cities = ['London', 'Birmingham', 'Leeds', 'Sheffield', 'Bradford', 'Manchester', 'Liverpool', 'Newcastle upon Tyne', 'Nottingham', 'Bristol', 'Brighton', 'Cambridge', 'Canterbury', 'Chester', 'Coventry', 'Durham', 'Exeter', 'Gloucester', 'Hull', 'Lancaster', 'Leicester', 'Lincoln', 'Oxford', 'Peterborough', 'Plymouth', 'Portsmouth', 'Reading', 'St Albans', 'Salisbury', 'Southampton', 'Swansea', 'Wolverhampton', 'York']

# Generate 1000 rows of dummy data
for i in range(100):
    firstname = fake.first_name()
    lastname = fake.last_name()
    points = random.randint(0, 100)
    location = random.choice(cities)
    c.execute(f"INSERT INTO volunteers (firstname, lastname, points, location) VALUES ('{firstname}', '{lastname}', {points}, '{location}')")

# Commit the changes to the database
conn.commit()

# Execute a SELECT statement to retrieve all rows from the table
c.execute("SELECT * FROM volunteers")

# Fetch all rows from the result set
rows = c.fetchall()

# Print the column names
print("ID\tFIRSTNAME\tLASTNAME\tPOINTS\tLOCATION")

# Print each row of data
for row in rows:
    print(f"{row[0]}\t{row[1]}\t\t{row[2]}\t\t{row[3]}\t{row[4]}")

# Close the connection
conn.close()
