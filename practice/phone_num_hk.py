# prgm to get input from user pf their friend name and number(in dictionary)
# and print them in sequence

n=int(input())
d={}
l={}
for i in range(n):
    x=input()
    l=x.split()
    d[l[0]]=l[1]

# print(d)
name=[]
a=0
while a!='':
    a=input()
    name.append(a)

# print(name)
lenght=len(name)
for i in range(0,lenght-1):
    if name[i] in d:
        print(name[i],"=",d[name[i]])
    else:
        print("Not found")
