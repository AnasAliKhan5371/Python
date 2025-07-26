#75_insert date from user

import psycopg2
def table():
    conn=psycopg2.connect(dbname="postgres",user="postgres",password="5371555",host="localhost",port="5432")
    cursor=conn.cursor()
    cursor.execute('''create table employees(Name text,ID int,Age int);''')

    print('table created successfully')
    conn.commit()
    conn.close()

def data():
    conn=psycopg2.connect(dbname="postgres",user="postgres",password="5371555",host="localhost",port="5432")
    cursor=conn.cursor()
    name=input('enter a name: ')
    id=input('enter an id: ')
    age=input('enter an age: ')
    query='''insert into employees(Name,ID,Age) values(%s,%s,%s);'''
    cursor.execute(query,(name,id,age))
    print('Data Added')
    conn.commit()
    conn.close()
data()