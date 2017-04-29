import socket
import threading
import MySQLdb
class ThreadedServer(object):
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.bind((self.host, self.port))
    def listen(self):
        self.sock.listen(5)
        while True:
            client, address = self.sock.accept()
            print "New Client Connected at: ", address
            client.settimeout(120)
            threading.Thread(target = self.listenToClient,args = (client,address)).start()

    def listenToClient(self, client, address):
        size = 1024
        while True:
            try:
                data = client.recv(size)
                if data:
					db = MySQLdb.connect("localhost","root","try","hackathon")
					cur=db.cursor()
					print "Client", address,"has sent data: "
					cur.execute(inp)
					db.commit()
					print "Database Updated of Data from Client: ",conn
                else:
                    raise error('Client disconnected')
            except:
                client.close()
                return False	   	
if __name__ == "__main__":
    port_num = 12353
    host='192.168.225.129'
    print "Server Starting at: ",host,port_num
    ThreadedServer(host,port_num).listen()
