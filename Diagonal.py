print("Bummer..!!")
import math
def pxt(val,crd,x1,x2,y1,y2):
        x3,x4=x1,x2
        y3,y4=y1,y2
        if(crd=="y"):
                x3=x4=(x1+val)
        elif(crd=="x"):
                y3=y4=(y1+val)
        print (x1,y1)
	print (x2,y2)
	print (x3,y3)
	print (x4,y4)
	print "%0.2f" % (math.sqrt(2*(val**2)))

x1 = input("first x coordinate : ")
y1 = input("first y coordinate : ")
x2 = input("second x coordinate : ")
y2 = input("second y coordinate : ")

x=cmp(x1,x2)
y=cmp(y1,y2)
if x==0:
	pxt(abs(y1-y2),"y",x1,x2,y1,y2)
else:
	pxt(abs(x1-x2),"x",x1,x2,y1,y2)
