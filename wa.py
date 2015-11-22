import psycopg2
 
import sys
import time
from datetime import datetime
import random
import re
import match
import os
import sendemail
import pclogging

sys.path.append('./Adafruit_Python_GPIO')
sys.path.append('./RTC_SDL_DS3231')
sys.path.append('./Adafruit_Python_BMP')
sys.path.append('./SDL_Pi_Weather_80422')
sys.path.append('./RaspberryPi-AS3935/RPi_AS3935')
sys.path.append('./SDL_Pi_INA3221')
sys.path.append('./SDL_Pi_TCA9545')

import SDL_Pi_INA3221
import SDL_DS3231
import Adafruit_BMP.BMP085 as BMP180
import SDL_Pi_Weather_80422 as SDL_Pi_Weather_80422

 
db_con = None

dt = datetime.now()
 
try:
 
  #Create a database session
 
  db_con = psycopg2.connect(database='postgres', user='pi', password='0')
 
  #Create a client cursor to execute commands
 
  cursor = db_con.cursor()
 
  #cursor.execute("CREATE TABLE customers (id SERIAL PRIMARY KEY, name VARCHAR, age INTEGER);")
 
  #The variables placeholder must always be a %s, psycop2 will automatically convert the values to SQL literal
 
  cursor.execute("INSERT INTO weathers ( temperature, humidity, content, created_at) VALUES (%s, %s, %s, %s)",(12, 26, "psycho", dt ))
 
  db_con.commit()
 
  cursor.execute("SELECT * FROM weathers order by created_at desc limit 1")
  print(cursor.fetchone())
 
except psycopg2.DatabaseError as e:
 
    print ('Error %s' % e    )
 
sys.exit(1)
 
 
if db_con:
 
  db_con.close()
