nl=[1,9,3,"ahmed"]
x=(1,2,3,4,"ali")
cl=list(x)
cl2=list((1,3,'s'))
#print(nl)
#print(cl)
#print(cl2)

c=[]
c.append(9)
c.insert(0,1)
c.extend([25,89,0])
#print(c)

c.pop(2)
#print(c)
c.remove(0)
#print(c)
c.clear()
#print(c)
del c
#print(c)

#print(nl)
nl.reverse()
#print(nl)
e=[]
list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]
a=0
for i in list1:
    e.append(list1[a]+list2[a])
    a=a+1


#print(e)
n=(i+j for i ,j in zip(list1,list2))
c=list(n)
#print(c)

sq=[1,2,3,4,5,6,7,8,9,10]
q=[]
for i in sq:
    q.append(i**2)
#print(q)

l1=[10,20,30]
l2=[100,200,300]
l2.sort()
for i, j in zip(l1,l2):
    print(i,j)
