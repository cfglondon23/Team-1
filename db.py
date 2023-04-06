import sqlite3
from faker import Faker
import random
import datetime
# Create a connection to the database
conn = sqlite3.connect('example.db', check_same_thread=False)

# Create a cursor object to execute SQL commands
c = conn.cursor()
c.execute("DROP table IF EXISTS volunteers;")
c.execute("DROP table IF EXISTS school;")
c.execute("DROP table IF EXISTS event;")
c.execute("DROP table IF EXISTS eventschool;")
# Create the volunteers table if it doesn't exist
c.execute('''CREATE TABLE IF NOT EXISTS volunteers
             (volunteerid INTEGER PRIMARY KEY, firstname TEXT, lastname TEXT, points INTEGER, location TEXT)''')
c.execute('''CREATE TABLE IF NOT EXISTS school
             (schid INTEGER PRIMARY KEY, location TEXT, city TEXT, name TEXT, info TEXT)''')
c.execute('''CREATE TABLE IF NOT EXISTS event
             (eventid INTEGER PRIMARY KEY, name TEXT, schid INT, info TEXT, complete TEXT, sofar INT, required INT, date DATE)''')
c.execute('''CREATE TABLE IF NOT EXISTS eventschool
             (eventid INTEGER PRIMARY KEY, schid INTEGER)''')


# Create a Faker instance to generate random names
fake = Faker()

# Define a list of real English city names
cities = ['London', 'Birmingham', 'Leeds', 'Sheffield', 'Bradford', 'Manchester', 'Liverpool', 'Newcastle upon Tyne', 'Nottingham', 'Bristol', 'Brighton', 'Cambridge', 'Canterbury', 'Chester', 'Coventry', 'Durham', 'Exeter', 'Gloucester', 'Hull', 'Lancaster', 'Leicester', 'Lincoln', 'Oxford', 'Peterborough', 'Plymouth', 'Portsmouth', 'Reading', 'St Albans', 'Salisbury', 'Southampton', 'Swansea', 'Wolverhampton', 'York']

# Generate 1000 rows of dummy data
for i in range(25):
    firstname = fake.first_name()
    lastname = fake.last_name()
    points = random.randint(0, 250)
    location = random.choice(cities)
    c.execute(f"INSERT INTO volunteers (firstname, lastname, points, location) VALUES ('{firstname}', '{lastname}', {points}, '{location}')")
# insert some mock data into the school table
schools = [(1, 'Oxford', 'Oxfordshire', 'Oxford High School', 'A leading independent girls\' school'), 
           (2, 'Windsor', 'Berkshire', 'Eton College', 'A prestigious independent boys\' boarding school'), 
           (3, 'London', 'Greater London', 'St Paul\'s School', 'An independent school for boys aged 7-18'), 
           (4, 'Elstree', 'Hertfordshire', 'Haberdashers\' Aske\'s Boys\' School', 'An independent day school for boys aged 5-18'), 
           (5, 'Cheadle Hulme', 'Greater Manchester', 'Cheadle Hulme School', 'A leading independent day school for boys and girls aged 3-18'), 
           (6, 'Rochester', 'Kent', 'St. John Fisher Catholic Primary School', 'A primary school in Rochester'), 
           (7, 'London', 'Greater London', 'St. Saviour\'s Church of England Primary School', 'A primary school in London'), 
           (8, 'Basingstoke', 'Hampshire', 'Great Binfields Primary School', 'A primary school in Basingstoke'), 
           (9, 'Manchester', 'Greater Manchester', 'Chorlton Park Primary School', 'A primary school in Manchester'), 
           (10, 'Limpsfield', 'Surrey', 'Hazelwood School', 'A co-educational school for children aged 3-13 in Surrey')]
c.executemany("INSERT INTO school (schid, location, city, name, info) VALUES (?, ?, ?, ?, ?)", schools)

events = [(1, 'Coding Workshop', random.randint(1, 5), 'Learn the basics of coding and programming', "TRUE", 10, 10, datetime.date(2022, 3,7)), 
          (2, 'Art and Design Exhibition', random.randint(1, 5), 'View and appreciate the creative talents of students', "TRUE", 5, 5,datetime.date(2023, 1,7)), 
          (3, 'Sports Day', random.randint(6, 10), 'Compete in a variety of athletic events and have fun', "TRUE", 4, 4,datetime.date(2023, 2,15)), 
          (4, 'Science Fair', random.randint(1, 5), 'Showcase and explore the wonders of science and technology', "FALSE", 1, 3, datetime.date(2023, 8,10)), 
          (5, 'Maths Challenge', random.randint(6, 10), 'Test your mathematical abilities in a fun and competitive environment', "FALSE", 2, 10, datetime.date(2023, 5,21)), 
          (6, 'Music Concert', random.randint(1, 10), 'Listen to talented musicians perform classical and contemporary pieces', "FALSE", 1, 12, datetime.date(2023, 6,30)), 
          (7, 'Drama Production', random.randint(1, 10), 'Watch aspiring actors showcase their acting skills in an exciting performance', "FALSE", 3, 7, datetime.date(2023, 12,24)), 
          (8, 'Charity Fundraiser', random.randint(1, 10), 'Raise money for a good cause and make a positive impact on the community', "FALSE", 3, 5,datetime.date(2023, 8,14)), ]
c.executemany("INSERT INTO event (eventid, name, schid, info, complete, sofar, required, date) VALUES (?, ?, ?, ?, ?, ?, ?, ?)", events)

# Commit the changes to the database
conn.commit()

# Execute a SELECT statement to retrieve all rows from the table

# Fetch all rows from the result set
rows = c.fetchall()

# Print the column names


# Close the connection






# commit changes and close the connection