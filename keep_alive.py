import http.server
import socketserver

PORT = 8000

class KeepAliveHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/alive':
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b'Bot is alive')
        else:
            self.send_response(404)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b'Not Found')

Handler = KeepAliveHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Keep-alive server running on port {PORT}")
    httpd.serve_forever()