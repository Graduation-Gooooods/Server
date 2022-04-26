import pymysql
import pymysql.cursors

connection = pymysql.connect(host='localhost', user='test_root', password='20171522',
                            db='test_mttb', charset='utf8', cursorclass=pymysql.cursors.DictCursor) # connenct db

cursor = connection.cursor()

sql_table_passive = """CREATE TABLE _passive(
                                md INT NOT NULL,
                                s1 INT NOT NULL,
                                s2 INT NOT NULL,
                                s3 INT NOT NULL,
                                s4 INT NOT NULL,
                                s5 INT NOT NULL,
                                cnt INT NOT NULL,
                                tm INT NOT NULL,
                                PRIMARY KEY(md)
                                );"""
sql_table_activate = """CREATE TABLE _automatic(
                                md INT NOT NULL,
                                scc INT NOT NULL,
                                tm INT NOT NULL,
                                cs INT NOT NULL,
                                PRIMARY KEY(md)
                                );"""
sql_table_trainning = """CREATE TABLE _training(
                                md INT NOT NULL,
                                req INT NOT NULL,
                                scc INT NOT NULL,
                                msc_mean INT NOT NULL,
                                tns_mean INT NOT NULL,
                                per_tm INT NOT NULL,
                                set_tm INT NOT NULL,
                                PRIMARY KEY(md)
                                );"""
                                
cursor.execute(sql_table_passive)
cursor.execute(sql_table_activate)    
cursor.execute(sql_table_trainning)

connection.close()  
