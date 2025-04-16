import sqlite3

db = sqlite3.connect('classroom.db')

c = db.cursor()

c.execute("INSERT INTO students VALUES('Mizan', 'Zafar', 'mizan.zafar2016@gmail.com')")

db.commit()

db.close()

