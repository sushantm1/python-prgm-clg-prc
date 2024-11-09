#prgm to check a number is palindrom or not
a=int(input("enter a number : "))
temp=a
temp1=0
while(a>0):
    remainder=a%10
    temp1=temp1*10 + remainder
    a=a//10

if(temp==temp1):
    print(temp1,"it's a palindrom number.")
else:
    print(temp1,"it's not a palindrom number.")