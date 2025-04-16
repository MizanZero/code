import sqlite3

db = sqlite3.connect('classroom.db')

# cursor(instance) was made
c = db.cursor()



db.commit() # commit changes to db

db.close()

