import http.server
import socketserver
import os

PORT = 8000

class CustomRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        # If the request is for a static model file
        if self.path.startswith('/static/'):
            # The base path for static files is the 'static' directory
            # We call the parent class's handler, but we do it from the root directory
            # so it correctly finds the 'static' folder.
            return http.server.SimpleHTTPRequestHandler.do_GET(self)
        
        # Otherwise, serve from the 'frontend' directory
        else:
            # We temporarily change the directory to 'frontend' to serve its files
            # This makes sure index.html and any other frontend assets are found
            original_cwd = os.getcwd()
            try:
                os.chdir(os.path.join(original_cwd, 'frontend'))
                # If root is requested, serve index.html
                if self.path == '/':
                    self.path = '/index.html'
                return http.server.SimpleHTTPRequestHandler.do_GET(self)
            finally:
                # IMPORTANT: Change back to the original directory
                os.chdir(original_cwd)

# Ensure we are in the script's directory before starting
os.chdir(os.path.dirname(os.path.abspath(__file__)))

with socketserver.TCPServer(("", PORT), CustomRequestHandler) as httpd:
    print(f"Server started at http://localhost:{PORT}")
    print("Serving 'frontend' directory and routing '/static/' requests.")
    print("Press Ctrl+C to stop the server.")
    httpd.serve_forever()

