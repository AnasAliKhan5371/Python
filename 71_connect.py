#71_Connect_to_Database

import psycopg2
connect=psycopg2.connect(dbname="postgres",user="postgres",password="5371555",host="localhost",port="5432")
print('connected successfully')

