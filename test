# Install and check working

## Install Database(MariaDB)
## Check working DB
## Check working test code
## Install PyMySQL 

import pymysql #pymysql support connection to db. especially mysql.

connection = pymysql.connect(host='localhost', user='test_root', password='20171522',
                             db='test', charset='utf8')

cursor = connection.cursor()

sql = "select * from member"
cursor.execute(sql)

rows = cursor.fetchall()
print(rows)

connection.close()
