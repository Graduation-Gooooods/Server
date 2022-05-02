#############################################
# 2022-04-24
# Get data from database
##############################################
import json
import socket
from http.server import HTTPServer, BaseHTTPRequestHandler
import urllib.parse as urlparser
import sqlControler

JSONTYPE = 'Application/json'
HOST = '192.168.0.14'
PORT = 2017

class requestHandler(BaseHTTPRequestHandler):
    def _get_headers(self): # 200 Okay header 
        self.send_response(200)
        self.send_header('Content-Type', JSONTYPE)
        self.end_headers()
        
    def _post_headers(self): # 201 Okay header 
        self.send_response(201)
        self.end_headers()
        
    def do_GET(self):
        querypath = urlparser.urlparse(self.path)
        path = querypath.path  
        user_path = path.split('/')[1]
        print(user_path)
        
        if user_path == 'app': # If Sender is App
            if path.endswith('/getpassive'):
                body = json.dumps(sqlControler.sqlControler.getPassive(), indent=4, sort_keys=True, default=str)
                self._get_headers()
                self.wfile.write(body.encode())
            elif path.endswith('/getauto'):
                body = json.dumps(sqlControler.sqlControler.getAutomatic(), indent=4, sort_keys=True, default=str)
                self._get_headers()
                self.wfile.write(body.encode())
            elif path.endswith('/gettraining'):
                body = json.dumps(sqlControler.sqlControler.getTraining(), indent=4, sort_keys=True, default=str)
                self._get_headers()
                self.wfile.write(body.encode())
                
                
    def do_POST(self):
        querypath = urlparser.urlparse(self.path)
        path = querypath.path  
        user_path = path.split('/')[1]
        print(user_path)
        
        content_length = int(self.headers['Content-Length'])
        
        body = self.rfile.read(content_length)
        body = body.decode()
        
        if 'mode' in body:
            mode = body[body.find('mode') + 9]
            print(mode)
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.sendto(mode.encode(), ("192.168.0.130", 2390))
        sock.close()
        self._post_headers()
        
        # elif 'chtension' in body:
        #     pass  
                            
try:            
    print("Starting HTTP server....")
    HTTPServer((HOST, PORT), requestHandler).serve_forever()
except KeyboardInterrupt:
    pass
print("Closed HTTP Server!!! Thank you.")
