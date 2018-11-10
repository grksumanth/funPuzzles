print "Burp!!"

consogram = [ 0 for _ in range(26)]

string = raw_input("please enter the String to compare : ")

for x in string:
	val = x.lower()
	cal = ord(val)-97
	if cal<26 and cal >0:
		consogram[cal]=1
consogram[0]=0
consogram[4]=0
consogram[8]=0
consogram[14]=0
consogram[20]=0
if sum(consogram) == 21:
	print "consogram suckers..!!"
else:
	print "LOL can't enter a consogram what a drag..!!"
