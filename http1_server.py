from http.server import SimpleHTTPRequestHandler, HTTPServer
import os

# Set the directory where files are stored
server_address = ("0.0.0.0", 8080)  # Listen on all interfaces
os.chdir("server_data")  # Change the directory to 'server_data' to serve files from there
print(os.getcwd())
handler = SimpleHTTPRequestHandler

with HTTPServer(server_address, handler) as httpd:
    print("Serving HTTP 1.1 on port 8080")
    httpd.serve_forever()
