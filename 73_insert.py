#72_insert date using pyyhon

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
    cursor.execute('''insert into employees(Name,ID,Age) values('Sam',01,22);''')

    print('Data Added')
    conn.commit()
    conn.close()
data()