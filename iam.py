from http.server import HTTPServer, SimpleHTTPRequestHandler
httpd = HTTPServer(('localhost', 7080), SimpleHTTPRequestHandler)
httpd.serve_forever()