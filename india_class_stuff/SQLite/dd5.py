import sqlite3
db=sqlite3.connect('simran.db')
cursor=db.cursor()
#id1=101
cursor.execute('select * from parikh where id=?',(200,))
record=cursor.fetchall()

for row in record:
         print('{0} {1}'.format(row[0],row[1]))
         
db.commit()
