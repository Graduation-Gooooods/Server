#############################################
# 2022-04-24
# Get data from database
##############################################

import json
import socket
from http.server import HTTPServer, BaseHTTPRequestHandler
import urllib.parse as urlparser
import sqlControler
import cgi

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
            elif path.endswith('/chmode1'):
                print(0)
                sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                print(1)
                sock.sendto('1'.encode(), ("192.168.0.130", 2390))
                print(2)
                # msg, _ = sock.recvfrom(2048)
                # print(msg.decode())
                sock.close()
                self._set_headers()
                
    def do_POST(self):
        # self.-_set_headers()
        # form = cgi.FieldStorage(
        #     fp=self.rfile,
        #     headers=self.headers,
        #     environ={'REAUEST_METHOD': 'POST'}
        # )
        querypath = urlparser.urlparse(self.path)
        path = querypath.path  
        user_path = path.split('/')[1]
        print(user_path)
        self._set_headers()
        
                            
try:            
    print("Starting HTTP server....")
    HTTPServer((host, port), requestHandler).serve_forever()
except KeyboardInterrupt:
    pass
print("Closed HTTP Server!!! Thank you.")
