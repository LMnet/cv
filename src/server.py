from http.server import HTTPServer, SimpleHTTPRequestHandler
from build import main_cv


port = 8099


class Handler(SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        html = main_cv.render()
        self.wfile.write(html.encode('utf-8'))


if __name__ == '__main__':
    # Test HTTP server to check rendered results
    server_address = ('', port)
    httpd = HTTPServer(server_address, Handler)
    print(f"Serving at port {port}")
    httpd.serve_forever()
