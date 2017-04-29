try:
	with open("data.txt",'r') as file1:
		a=file1.read()
except:
	print "File opening error"
finally:
	file1.close()
a=a.split('\n')
for fn in a:
	s=fn.split(',')
	sub=s[0]
	vo=(s[1])
	cu=(s[2])
	pw=(s[3])
	fr=(s[4])
	pf=(s[5])
	et=(s[6])
	dt=s[7]
	cmd="insert into power_data values('"+sub+"',"+vo+","+cu+","+pw+","+fr+","+pf+","+et+","+dt+");"
	print cmd
