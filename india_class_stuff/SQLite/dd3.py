import sqlite3
db=sqlite3.connect('sammy1.db')
a=100
a1="yash"

cursor=db.cursor()
cursor.execute('insert into abc(id,name) values (:id,:name)',{'id':a,'name':a1})
db.commit()
