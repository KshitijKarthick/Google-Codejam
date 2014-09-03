#! /usr/bin/env/python
def search(key,i,num):
	while i<len(num):
		print num[i],key
		if(key == num[i]):
			print "true"			
			return i
		i=i+1
	return -1
f1=open("new1.in","r")
f2=open("new1.out","w")
list=(f1.read()).split("\n")
total=long(list[0])
del list[0]
i=long(0)
j=long(0)
flag=1
num=range(0,4)
while i<total:
	n=list[0]
	del list[0]
	l=list[0].split(" ");
	print l
	while j<num:
		print l[j],j,num
		ele=search(l[j],j,num)
		print ele
		if ele==-1:
			flag=0
			s="Case #"+str(i)+": "+"BAD"+"\n"
            		f2.write(s)
           		break
		print "NUM[J]:",num[j]
		temp=num[j]
		num[j]=num[ele]
		print "NUM[ele]:",num[ele]
		num[ele]=temp
		j=j+1
	if flag==1:
		s="Case #"+str(i)+": "+"GOOD"+"\n"
            	f2.write(s)
	flag=1
	i=i+1
f1.close()
f2.close()
    
   
