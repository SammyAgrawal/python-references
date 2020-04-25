import pandas as pd
#df=pd.read_csv("nagar3.csv")
import sqlite3
import sqlalchemy
engine=sqlalchemy.create_engine('c:\python3.6.4\gunjan.db')
df=pd.read_sql_table("jha",engine)
print(df)
