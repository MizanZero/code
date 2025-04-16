import sqlite3

db = sqlite3.connect('classroom.db')

c = db.cursor()

# querying the db
c.execute("SELECT * FROM students")

""" Fetching returns a tuple """
# fetch one (0th index by default)
index = 0
#print(c.fetchone()[index]) 

# fetch as many as specified
#print(c.fetchmany(2)) 

# fetch all
#print(c.fetchall()) 

