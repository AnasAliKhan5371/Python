#72_Create table using python

import psycopg2

conn=psycopg2.connect(dbname="postgres",user="postgres",password="5371555",host="localhost",port="5432")
cursor=conn.cursor()
cursor.execute('''create table employees(Name text,ID int,Age int);''')

print('table created successfully')
conn.commit()
conn.close()