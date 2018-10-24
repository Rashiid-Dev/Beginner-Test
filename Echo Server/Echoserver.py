from http.server import HTTPServer, BaseHTTPRequestHandler

class EchoHandler(BaseHTTPRequestHandler):
	def do_GET(self):
		#sends a 200 OK response
		self.send_response(200)
        #Sends Headers
		self.send_header("Content-type", "text/plain; utf-8")
		self.end_headers()
		# Writes the response body
		self.wfile.write(self.path[1:].encode())

if __name__ == "__main__":
	server_address = ("", 8000) #Serve on all addresses, port 8000
	httpd = HTTPServer(server_address, EchoHandler)
	httpd.serve_forever()

