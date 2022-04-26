#############################################
# 2022-04-26
# Make data to database
##############################################

import pymysql
import random

HOST = 'localhost'
USER = 'test_root'
PWD = '2018'
DB = 'test'


connection = pymysql.connect(host=HOST, user=USER, password=PWD,
                             db=DB, charset='utf8')


mdarr = []
for i in range(10):
    mdarr.append(random.randint(1, 50))
    
sccarr = []
for i in range(10):
    sccarr.append(random.randint(1, 50))

tmarr = []
for i in range(10):
    tmarr.append(random.randint(1, 50))
    
csarr = []
for i in range(10):
    csarr.append(random.randint(1, 50))
    
sql = '''INSERT into _automatic(md, scc, tm, cs)
            VALUE (%i, %i, %i, %i)'''

cursor = connection.cursor()

for i in range(10):
    cursor.execute(sql, (mdarr[i], sccarr[i], tmarr[i], csarr[i]))
    connection.commit
    
connection.close()
