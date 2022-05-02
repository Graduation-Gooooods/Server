# import for connection database
import pymysql
import pymysql.cursors
# connect to database
connection = pymysql.connect(host='localhost', user='test_root', password='20171522',
                            db='test_tb', charset='utf8', cursorclass=pymysql.cursors.DictCursor) # connenct db
cursor = connection.cursor()
# class for control maria db
class sqlControler():
    def __init__(self):
        print("Making sql controler")
        
    #  for app   
    def getAutomatic():
        sql = "SELECT * FROM _automatic WHERE mode = 0 ORDER BY date_time  DESC LIMIT 10;"
        cursor.execute(sql) # send sql line to db server 
        data = cursor.fetchall()  # fetchall, fetchone, fetchmany...
        return data
    def getPassive():
        sql = "SELECT * FROM _passive WHERE mode = 1 ORDER BY date_time  DESC LIMIT 10;"
        cursor.execute(sql) # send sql line to db server 
        data = cursor.fetchall()  # fetchall, fetchone, fetchmany...
        return data
    def getTraining():
        sql = "SELECT * FROM _training WHERE mode = 2 ORDER BY date_time  DESC LIMIT 10;"
        cursor.execute(sql) # send sql line to db server 
        data = cursor.fetchall()  # fetchall, fetchone, fetchmany...
        return data
    # for arduino
    def getPreviousMode():
        sql = "SELECT mode FROM _intergration ORDER BY date_time DESC LIMIT 1"
        cursor.execute(sql)
        data = cursor.fetchone()
        data = data["mode"]
        return data
    
    def insertPssvData(mode, scc, s1, s2, s3, s4, s5, ex_time):
        sql = "INSERT INTO _intergration(mode, date_time, scc, s1, s2, s3, s4, s5, ex_time) \
            VALUES(%s, now(), %s, %s, %s, %s, %s, %s, %s)"
        cursor.execute(sql, (mode, scc, s1, s2, s3, s4, s5, ex_time))
        connection.commit()
        print(f"Success {mode}: {scc}, {s1}, {s2}, {s3}, {s4}, {s5}, {ex_time}")
    
    def insertAutoData(mode, scc, now_step, ex_time):
        sql = "INSERT INTO _intergration(mode, date_time, scc, now_step, ex_time) \
            VALUES(%s, now(), %s, %s, %s)"
        cursor.execute(sql, (mode, scc, now_step, ex_time))
        connection.commit()
        print(f"Success {mode}: {scc}, {now_step}, {ex_time}")
        
    def insertTrnData(mode, scc, now_step, req, per_time, set_time, msc_mean, tns_mean, ex_time):
        sql = "INSERT INTO _intergration(mode, date_time, scc, now_step, req, per_time, set_tiem, msc_mean, tns_mean) \
            VALUES (%s, now(), %s, %s, %s, %s, %s, %s)"
        cursor.execute(sql, (mode, scc, now_step, req, per_time, set_time, msc_mean, tns_mean, ex_time))
        connection.commit()
        print(f"Success {mode}: {per_time}, {set_time}, {msc_mean}, {tns_mean}")
        
        
        
        
   
    