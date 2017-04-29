import sys, socket
import MySQLdb
from threading import Thread

host="192.168.225.129"
port=12355
s=socket.socket()
s.bind((host,port))
s.listen(5)
threads=[]
print "server is running on + ",host,port
db = MySQLdb.connect("localhost","root","try","hackathon")
cur=db.cursor()
c,a=s.accept()
while True:
#	c,a=s.accept()
	print "Connection Recieved from Client: ", a
	inp=c.recv(1024)
	print "data recieved", inp
	try:
		cur.execute(inp)
		db.commit()
		print "Database Updated of Data from Client: ",a
	except:
		db.rollback()
		print "Database Failed to be Updated of Data from Client: ",a

s.close()
c.close()

