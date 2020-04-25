import sqlite3
db=sqlite3.connect('sammy1.db')
cursor=db.cursor()

cursor.execute('select * from abc')
s=cursor.fetchall()
for row in s:
         print('{0}:{1}'.format(row[0],row[1]))
         
db.commit()
