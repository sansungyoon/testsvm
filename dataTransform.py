f=open("./0116_setting.txt",'r')
data=f.read().split(",")
data=map(float,data)
f.close()
x=[]
X=[]
y=[]

for i in range(len(data)):
	if (i%5==4):
		y.append(data[i])
	else:
		x.append(data[i])

X=zip(x[0::4],x[1::4],x[2::4],x[3::4])
y=map(int,y)

#print X
#print y

