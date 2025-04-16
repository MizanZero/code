import sqlite3

db = sqlite3.connect('classroom.db')

# cursor(instance) was made
c = db.cursor()

c.execute("""CREATE TABLE students(
    first_name text,
    last_name text,
    roll_no text
)""")

db.commit() # commit changes to db

db.close()

