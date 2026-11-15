from http.server import BaseHTTPRequestHandler, HTTPServer


class Handler(BaseHTTPRequestHandler):
    def do_POST(self):
        size = int(self.headers.get('Content-Length', 0))
        body = self.rfile.read(size).decode()
        has_token = bool(self.headers.get('Authorization'))
        print('NOTIFICATION: ' + body + ' | token sent: ' + str(has_token), flush=True)
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b'ok')

    def log_message(self, *args):
        pass


HTTPServer(('0.0.0.0', 9000), Handler).serve_forever()