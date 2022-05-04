#############################################
# 2022-05-04 server
# using sqlControler
# fin
##############################################
from http.server import HTTPServer, BaseHTTPRequestHandler
import json
import socket
import urllib.parse as urlparser
import sqlControler

JSONTYPE = 'Application/json'
HOST = '192.168.0.14' # Open IP_ADDR
PORT = 2017           # Open PORT 

class requestHandler(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200) # 200 OK
        self.send_header('Content-Type', JSONTYPE) # content type
        self.end_headers() # header finish
        
    def do_GET(self):
        querypath = urlparser.urlparse(self.path)
        path = querypath.path  
        print(f'Total path: {path}')
        user_path = path.split('/')[1]
        print(f'User path: {user_path}')
        
        if user_path == 'get': # Return 10 latest data for that mode
            if path.endswith('/passive'):
                body = { 'total':sqlControler.sqlControler.getPassive() }
                body = json.dumps(body, indent=4, sort_keys=True, default=str)
                self._set_headers()
                self.wfile.write(body.encode())
            elif path.endswith('/auto'):
                body = { 'total':sqlControler.sqlControler.getAutomatic() }
                body = json.dumps(body, indent=4, sort_keys=True, default=str)
                self._set_headers()
                self.wfile.write(body.encode())
            elif path.endswith('/training'):
                body = { 'total':sqlControler.sqlControler.getTraining() }
                body = json.dumps(body, indent=4, sort_keys=True, default=str)
                self._set_headers()
                self.wfile.write(body.encode())
            print(f'Complete send 10 data {user_path}')
        
        elif user_path == 'set': # Adjust the tension on the finger
            finger, tension = path.split('/')[2], path.split('/')[3]
            data = 's' + finger + tension
            print(data)
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            sock.sendto(data.encode(), ("192.168.0.137", 2390))
            sock.close()
            self._set_headers()
            print(f'Complete {user_path} tension')
        
        elif user_path == 'chmode': # Change mode
            mode = path.split('/')[2]
            data = 'm' + mode
            print(mode)
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            sock.sendto(data.encode(), ("192.168.0.137", 2390))
            sock.close()
            self._set_headers()
            print(f'Complete {user_path}')
                
                            
try:            
    print("Starting HTTP server....")
    HTTPServer((HOST, PORT), requestHandler).serve_forever()
except KeyboardInterrupt:
    print("Closed HTTP Server!!! Thank you.")
