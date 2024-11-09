#prgm to check a number is not a armstrong no. or not
a=int(input("enter a number : "))
length=len(str(a))
same=a
temp1=0
while(a>0):
    remain=a%10
    temp1=temp1 + (remain**length)
    a=a//10
if(same==temp1):
    print(temp1,"it's a armstron number.")
else:
    print(temp1,"it's not a armstrong number.")