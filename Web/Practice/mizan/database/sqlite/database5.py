import sqlite3

db = sqlite3.connect('classroom.db')

# cursor(instance) was made
c = db.cursor()

"""Each row has a row id before it in the first coloumn"""


db.commit() # commit changes to db

db.close()

