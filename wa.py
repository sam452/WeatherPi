import psycopg2
 
import sys
 
db_con = None
 
try:
 
  #Create a database session
 
  db_con = psycopg2.connect(database='postgres', user='pi', password='0')
 
  #Create a client cursor to execute commands
 
  cursor = db_con.cursor()
 
  #cursor.execute("CREATE TABLE customers (id SERIAL PRIMARY KEY, name VARCHAR, age INTEGER);")
 
  #The variables placeholder must always be a %s, psycop2 will automatically convert the values to SQL literal
 
  cursor.execute("INSERT INTO weathers ( temperature, humidity, content) VALUES (%s, %s, %s)",(12, 26, "psycho"))
 
  db_con.commit()
 
  cursor.execute("SELECT * FROM weathers order by created_at desc limit 1")
  print(cursor.fetchone())
 
except psycopg2.DatabaseError as e:
 
    print ('Error %s' % e    )
 
sys.exit(1)
 
 
if db_con:
 
  db_con.close()