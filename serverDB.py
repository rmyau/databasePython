from http.server import HTTPServer
#from http.server import CGIHTTPServer
from http.server import CGIHTTPRequestHandler
import BD

def main():
    # db.setup_tables()
    # db.add_test_data()
    server_addr = ('0.0.0.0', 8000)
    handler = CGIHTTPRequestHandler
    handler.cgi_directories = ["/cgi-bin"]
    server = HTTPServer(server_addr, handler)
    server.serve_forever()
main()

