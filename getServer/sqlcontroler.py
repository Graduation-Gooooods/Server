import pymysql
import pymysql.cursors

connection = pymysql.connect(host='localhost', user='test_root', password='20171522',
                            db='test_tb', charset='utf8', cursorclass=pymysql.cursors.DictCursor) # connenct db
cursor = connection.cursor()

class sqlControler():
    def __init__(self):
        print("Maked sql controler")
        
       
    def getData():
        sql = "SELECT * FROM _intergration ORDER BY date_time  DESC LIMIT 10;"
        cursor.execute(sql) # send sql line to db server 
        data = cursor.fetchall()  # fetchall, fetchone, fetchmany...
        return data
    
    def createAuto(scc, cs, tm, md):
        sql = "INSERT INTO _automatic(scc, cs, tm, md) VALUES(%s, %s, %s, %s)"
        cursor.execute(sql, (scc, cs, tm, md)) # send sql line to db server 
        complete = connection.commit()
        print(complete)
        return complete
    
    def getPriviousMode():
        pass   
    
