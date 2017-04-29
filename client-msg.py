import socket,sys
s=socket.socket()
host=socket.gethostname()
port=12352
s.connect((host,port))
inp=raw_input()
print type(inp)
s.sendall(inp)
print s.recv(1024)
s.close()