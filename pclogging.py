#
#
# logging system from Project Curacao 
# filename: pclogger.py
# Version 1.0 10/04/13
#
# contains logging data 
#


CRITICAL=50
ERROR=40
WARNING=30
INFO=20
DEBUG=10
NOTSET=0


import sys
import time
#import psycopg2 as mdb

DATABASEPASSWORD = "0"

def log(level, source, message):

   LOWESTDEBUG = 0
	# open mysql database

	# write log


	# commit


	# close

   if (level >= LOWESTDEBUG):
        try:
	
                #print("trying database")
                con = mdb.connect(database='postgres', user='pi', password='0');

                cur = con.cursor()
                print "before query"

                query = "INSERT INTO systemlog(Level, Source, Message) VALUES(%i, '%s', '%s')" % (level, source, message)
	        print("query=%s" % query)

                cur.execute(query)

                con.commit()


        except mdb.DatabaseError as e:

                print ('Error %s' % e    )
                con.rollback()
                #sys.exit(1)

        finally:
                cur.close()
                con.close()

                del cur
                del con

