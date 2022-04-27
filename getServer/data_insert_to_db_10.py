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

sql = "INSERT INTO _intergration(mode, date_time, scc, now_step, ex_time) VALUES(1, now(), 25, 5, 25)"
sql = "INSERT INTO _intergration(mode, date_time, ex_time, scc, s1, s2, s3, s4, s5) VALUES(0, now(), 30, 14, 3, 3, 2, 1, 4)"
sql = "INSERT INTO _intergration(mode, date_time, scc, now_step, ex_time) VALUES(1, now(), 30, 5, 30)"
sql = "INSERT INTO _intergration(mode, date_time, scc, now_step, ex_time) VALUES(1, now(), 27, 6, 29)"
sql = "INSERT INTO _intergration(mode, date_time, ex_time, scc, s1, s2, s3, s4, s5) VALUES(0, now(), 30, 14, 4, 5, 2, 2, 4)"
sql = "INSERT INTO _intergration(mode, date_time, scc, now_step, ex_time) VALUES(1, now(), 26, 6, 28)"
sql = "INSERT INTO _intergration(mode, date_time, scc, now_step, ex_time) VALUES(1, now(), 29, 7, 27)"
sql = "INSERT INTO _intergration(mode, date_time, ex_time, scc, s1, s2, s3, s4, s5) VALUES(0, now(), 30, 14, 4, 4, 2, 2, 4)"
sql = "INSERT INTO _intergration(mode, date_time, ex_time, scc, now_step, req, per_time, set_time, msc_mean, tns_mean) VALUES(2, now(), 300, 23, 5, 25, 4, 13, 220, 56)"
sql = "INSERT INTO _intergration(mode, date_time, ex_time, scc, s1, s2, s3, s4, s5) VALUES(0, now(), 30, 14, 4, 6, 2, 2, 4)"
sql = "INSERT INTO _intergration(mode, date_time, ex_time, scc, s1, s2, s3, s4, s5) VALUES(0, now(), 30, 14, 3, 3, 2, 1, 4)"

cursor.execute(sql, (20, 20, 20, 20))

connection.commit()

connection.close()


