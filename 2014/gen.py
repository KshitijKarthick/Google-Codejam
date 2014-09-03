#! /usr/bin/env/python
import random
print "\nEnter Output FileName"
f1=open(str(raw_input()),"w")
i=long(0)
f1.write("10000\n")
while i<10000:
    line=str(random.randint(1,10000))+" "+str(random.randint(1,1000))+" "+str(random.randint(1,1000000))+"\n"
    f1.write(line)
    i=i+1
f1.close()
