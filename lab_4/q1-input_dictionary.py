# Python Program to Add a Key-Value Pair to the Dictionary
x=int(input("enter the size of dictionary = "))
d={}
for i in range(0,x):
    a=input("enter the keys and values  " )
    l=[]
    l=a.split()
    d[l[0]]=l[1]
print(d)

