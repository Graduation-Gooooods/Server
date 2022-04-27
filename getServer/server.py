#############################################
# 2022-04-24
# Get data from database
##############################################

import json
from datetime import datetime, date
from http.server import HTTPServer, BaseHTTPRequestHandler
import urllib.parse as urlparser
import sqlControler

cont_type = 'Content-type'
jsontype = 'Application/json'
host = '192.168.0.14'
port = 2017

class requestHandler(BaseHTTPRequestHandler):
    def _set_headers(self): # 200 Okay header 
        self.send_response(200)
        self.send_header(cont_type, jsontype)
        self.end_headers()
        
    def do_GET(self):
        querypath = urlparser.urlparse(self.path)
        path = querypath.path  
        user_path = path.split('/')[1]
        print(user_path)
        
        if user_path == 'app': # If Sender is App
            if path.endswith('/getdata'):
                body = json.dumps(sqlControler.sqlControler.getData(), indent=4, sort_keys=True, default=str)
                self._set_headers()
                self.wfile.write(body.encode())
        
        elif user_path == 'jamjam': # If Sender is Jamjam
            if path.endswith('/priviousmode'):
                body = json.dumps(sqlControler.sqlControler.getPriviousMode())
                self._set_headers()
                self.wfile.write(body.encode())
            
        else: # Not App or Jamjam
            self.send_response(404)
            self.end_headers()
            
                   
    def do_POST(self):
        querypath = urlparser.urlparse(self.path)
        path, query = querypath.path, querypath.query
        print(path, query)
        
        if path.endswith('/createauto'):
            sqlControler.sqlControler.createAuto(scc=10, tm=160, cs=4, md=1)
            self._set_headers()
            dic = {"rsp": "success"}
            self.wfile.write(json.dumps(dic).encode())
            
        
HTTPServer((host, port), requestHandler).serve_forever()
