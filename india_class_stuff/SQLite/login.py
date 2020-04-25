import sqlite3 as sql
db=sql.connect('login.db')
cursor=db.cursor()# takes query, executes in db
cursor.execute("CREATE TABLE if not exists users(username text primary key, password text)")
def register():
    user = input("Whas gon be ur username ")
    passw = input("Whas gon be ur password ")
    cursor.execute('INSERT INTO users(username, password) values (?,?)', (user, passw))
db.commit()
register()

