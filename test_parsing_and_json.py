
#############################################
# 2022-04-03
# Gettingg data from database
# Sending data format : JSON
# parsing [IP_ADDR]/dsr dsr
##############################################

import pymysql
import pymysql.cursors
import json
# import http
import socket 


connection = pymysql.connect(host='localhost', user='test_root', password='20171522',
                            db='test', charset='utf8', cursorclass=pymysql.cursors.DictCursor) # connenct db
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # open socket
s.bind(('', 2017)) # binding
s.listen(2) # waiting listen


# while True:
client, addr = s.accept()
print('Connection from ', addr)
# client.send(b'Hi')

data = client.recv(1024)
msg = data.decode()
print(data)
req = msg.split('\r\n')

req = req[0].split(' ')
print(req)
req_gp = req[0]
print(req_gp)
req = req[1].split('/')
# print(req)
req = req[1]
print(req)

cursor = connection.cursor() # get cursor from connection object

sql = "SELECT * FROM member"
cursor.execute(sql) # send sql line to db server 

rows = cursor.fetchall()  # fetchall, fetchone, fetchmany...
print(rows)
json_val = json.dumps(rows)

if req == 'data':
    print(req)
    # f = open("index.html", 'r', encoding='utf-8')
    mimetype = 'application/json' 
    
    client.send(b'HTTP/1.1 200 OK\r\n')
    client.send(b'Content-Type: ' + mimetype.encode() + b'\r\n')
    client.send(b'\r\n')
    client.sendall(json_val.encode())
    # data = f.read()
    # client.send(data.encode('euc-kr'))
        
    connection.close()
    client.close()
    
