import http.server, os, socketserver

class H(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        p = self.path.split('?')[0]
        if p == '/' or not os.path.isfile('.' + p):
            self.path = '/index.html'
        return super().do_GET()

socketserver.ThreadingTCPServer.allow_reuse_address = True
socketserver.ThreadingTCPServer(('', 5173), H).serve_forever()
