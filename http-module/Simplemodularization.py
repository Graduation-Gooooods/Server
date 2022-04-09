#############################################
# 2022-04-08
# Get data from database
# Access Multiple Tables
##############################################

import mimetypes
from socketserver import BaseRequestHandler
import pymysql
import pymysql.cursors
import json
from http.server import HTTPServer, BaseHTTPRequestHandler
import urllib.parse as urlparser

cont_type = 'Content-type'
mimetype = 'Application/json'
host = 'localhost'
port = 2017

connection = pymysql.connect(host='localhost', user='test_root', password='20171522',
                            db='test_mttb', charset='utf8', cursorclass=pymysql.cursors.DictCursor) # connenct db
cursor = connection.cursor()

class sqlControler():
    print("Maked sql controler")
    
    def auto():
        sql = "SELECT * FROM _automatic"
        cursor.execute(sql) # send sql line to db server 
        data = cursor.fetchall()  # fetchall, fetchone, fetchmany...
        return data


class requestHandler(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header(cont_type, mimetype)
        self.end_headers()
        
    def do_GET(self):
        querypath = urlparser.urlparse(self.path)
        path, query = querypath.path, querypath.query
        print(path, query)
        
        if path.endswith('/getauto'):
            body = json.dumps(sqlControler.auto())
            self._set_headers()
            self.wfile.write(body.encode())
        
HTTPServer((host, port), requestHandler).serve_forever()
