import pymysql
import pymysql.cursors

connection = pymysql.connect(host='localhost', user='test_root', password='20171522',
                            db='test_tb', charset='utf8', cursorclass=pymysql.cursors.DictCursor) # connenct db

cursor = connection.cursor()

sql_table = """CREATE TABLE _intergration(
                                mode INT NOT NULL,
                                date_time DATETIME NOT NULL,
                                ex_time INT NULL,
                                scc INT NULL,
                                now_step INT NULL,
                                s1 INT  NULL,
                                s2 INT  NULL,
                                s3 INT  NULL,
                                s4 INT  NULL,
                                s5 INT  NULL,
                                req INT NULL,
                                per_time INT NULL,
                                set_time INT NULL,
                                msc_mean INT NULL,
                                tns_mean INT 
                                )"""

                                
cursor.execute(sql_table)


connection.close()  
