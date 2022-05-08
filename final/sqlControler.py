import pymysql
import pymysql.cursors

connection = pymysql.connect(host='localhost', user='test_root', password='20171522',
                            db='test_tb', charset='utf8', cursorclass=pymysql.cursors.DictCursor) # connenct db
cursor = connection.cursor()

class sqlControler():
    def __init__(self):
        print("Making sql controler")
        
    def getPassive():
        sql = "SELECT * FROM _intergration WHERE mode = 0 ORDER BY date_time  DESC LIMIT 10;"
        cursor.execute(sql) # send sql line to db server 
        data = cursor.fetchall()  # fetchall, fetchone, fetchmany...
        return data
    def getAutomatic():
        sql = "SELECT * FROM _intergration WHERE mode = 1 ORDER BY date_time  DESC LIMIT 10;"
        cursor.execute(sql) # send sql line to db server 
        data = cursor.fetchall()  # fetchall, fetchone, fetchmany...
        return data
    def getTraining():
        sql = "SELECT * FROM _intergration WHERE mode = 2 ORDER BY date_time  DESC LIMIT 10;"
        cursor.execute(sql) # send sql line to db server 
        data = cursor.fetchall()  # fetchall, fetchone, fetchmany...
        return data
####################################################################    
    def getPreviousMode():
        sql = "SELECT mode FROM _intergration ORDER BY date_time DESC LIMIT 1"
        cursor.execute(sql)
        data = cursor.fetchone()
        mode = data["mode"]
        return mode
    
    def getStep():
        sql = "SELECT now_step FROM _intergration ORDER BY date_time DESC LIMIT 1"
        cursor.execute(sql)
        data = cursor.fetchone()
        step = data["now_step"]
        return step
    
    def insertPssvData(mode, s1, s2, s3, s4, s5, scc, ex_time):
        print(mode, s1, s2, s3 ,s4 ,s5, scc, ex_time)
        sql = "INSERT INTO _intergration(mode, date_time, scc, s1, s2, s3, s4, s5, ex_time) \
            VALUES(%s, now(), %s, %s, %s, %s, %s, %s, %s)"
        cursor.execute(sql, (mode, scc, s1, s2, s3, s4, s5, ex_time))
        connection.commit() 
        print(f"Success {mode}: {s1}, {s2}, {s3}, {s4}, {s5}, {scc}, {ex_time}")
    
    def insertAutoData(mode, now_step, scc, ex_time):
        sql = "INSERT INTO _intergration(mode, date_time, scc, now_step, ex_time) \
            VALUES(%s, now(), %s, %s, %s)"
        cursor.execute(sql, (mode, scc, now_step, ex_time))
        connection.commit()
        print(f"Success {mode}: {scc}, {now_step}, {ex_time}")
        
    def insertTrnData(mode, now_step, scc, ex_time, req, per_time, set_time, msc_mean, tns_mean):
        sql = "INSERT INTO _intergration(mode, date_time, now_step, scc, ex_time, req, per_time, set_time, msc_mean, tns_mean) \
            VALUES(%s, now(), %s, %s, %s, %s, %s, %s, %s, %s)"
        cursor.execute(sql, (mode, now_step, scc, ex_time, req, per_time, set_time, msc_mean, tns_mean))
        connection.commit()
        print(f"Success {mode}: {req}, {per_time}, {set_time}, {msc_mean}, {tns_mean}")
        
        
        
        
   
    
