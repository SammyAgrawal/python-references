import sqlite3
db=sqlite3.connect('sammy1.db')
cursor=db.cursor()

cursor.execute("create table if not exists abc(id integer primary key, name text)")
a= int(input("How many items want to add to database? "))
#? placeholder
for i in range(a):
    user_id = input("what id do u want for row ")
    user_name = input("what name do u want for row ")
    cursor.execute('insert into abc (id, name) values (?,?)',(user_id,user_name))
    
#cursor.execute('insert into abc (id) values (?)',(2,))

#cursor.execute('drop table jha')
db.commit()
