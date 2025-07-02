import os
import sys
import sqlite3

os.chdir(os.path.dirname(os.path.abspath(sys.argv[0])))
filePath = os.getcwd().replace('\\', '/') + "/static/users.db"
print(f"file path: {filePath}")

if not os.path.isfile(filePath):
    with open(filePath, 'w') as file:
        pass

try:
    connection = sqlite3.connect(filePath)
    cursor = connection.cursor()
    cursor.execute("CREATE TABLE user(IP)")
    connection.commit()
except:
    pass

ipList = cursor.execute("SELECT ip FROM user")

users = ipList.fetchall()

print(users)