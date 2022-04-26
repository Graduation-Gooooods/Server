#############################################
# 2022-04-26
# Make data to database
##############################################

import pymysql

HOST = 'localhost'
USER = 'test_root'
PWD = '20171522'
DB = 'test_mttb'


connection = pymysql.connect(host=HOST, 
                             user=USER, 
                             password=PWD,
                             db=DB, 
                             charset='utf8')
cursor = connection.cursor()

sql = "INSERT INTO _automatic (md, scc, tm, cs) VALUES (%s, %s, %s, %s)"

lst = []

for i in range(12, 20):
    md = i; scc = i; tm = i; cs = i
    val = (md, scc, tm, cs)
    lst.append(val)
    

cursor.executemany(sql, lst)

connection.commit()

connection.close()


