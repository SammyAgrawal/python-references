import sqlite3
db=sqlite3.connect('login.db')
cursor=db.cursor()# takes query, executes in db
cursor.execute('create table users(username text primary key, password text)')
#cursor.execute('drop table jha')
db.commit()
