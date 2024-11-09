#prgm to find it's factorial
a=int(input("enter the number : "))
tem=a
temp=1
while(a>0):
    temp=temp*a
    a=a-1
print("the factorial of",tem,"is : ",temp)
