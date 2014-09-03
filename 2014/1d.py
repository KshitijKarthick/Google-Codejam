#! /usr/bin/env/python
f1=open("1d.in","r")
f2=open("1d.out","w")
n=long(f1.readline())
#print n
i=long(0)
l1=[]
l2=[]
j=long(0)
k=long(0)
count=long(0)
while i<n:
    t=long(f1.readline())
    print t
    l1=(f1.readline()).split()
    print l1
    l2=(f1.readline()).split()
    print l2
    l1.sort()
    l2.sort()
    i=i+1
    while j<t:
        while k<t and flag:
            print "test",(l1[j]<l2[k])and( len(l1) or  len(l2))
            if((l1[j]<l2[k])and( len(l1) and  len(l2))):
                print l1,l2
                del l1[j]
                del l2[k]
                print l1,l2
                print count+1
                count=count+1
                break
            k=k+1
        j=j+1
    print "Count:",count
    print "List 1:",l1
    print "List 2:",l2  
    count=0
    j=0
    k=0
f1.close
f2.close
