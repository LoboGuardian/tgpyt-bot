# web.py
from http.server import BaseHTTPRequestHandler, HTTPServer  # http server 
import threading


class web:

  Port = 8080
  def __init__(self,port = -1):
    if (port != -1): self.Port = port

  def startThread(self):
    x = threading.Thread(target=self.Start)
    x.start()
    
  def Start(self):
      httpd = HTTPServer(('', self.Port),self.handler)
      httpd.serve_forever()

  class handler(BaseHTTPRequestHandler):
      def do_GET(self):
          self.send_response(200)
          self.send_header('Content-type', 'text/html')
          self.end_headers()

          message = "Bot ✅"
          self.wfile.write(bytes(message, "utf8"))
