#wap as a limit and display total no. of term of following series(fabonaci series)
a=int(input("enter a number : "))
first=0
second=1
temp=0
print(temp)
while(a>0):
    temp=first+second
    first=second
    second=temp
    a=a-1
    print(temp)
