import sqlite3

db = sqlite3.connect('classroom.db')

c = db.cursor()

multiple_students = [
                        ('Pritam', 'Idk', 'pritam.idk@gmail.com'),
                        ('Ayaan', 'Ahmed', 'ayaanahmed@gmail.com')
                    ] 

c.executemany("INSERT INTO students VALUES (?,?,?)", multiple_students)
# each question mark is a ('first_nm', 'last_nm', 'email')

db.commit()

db.close()

