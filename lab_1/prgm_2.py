# wap to find a number is palinderom or not "12321"
# #prgm to revers a number
a=int(input("Enter a unmber : "))
temp=a
temp2=0
while(a>0):
    remainder=a%10
    temp2= temp2*10 + remainder
    a=a//10

print(temp2)
# if(temp2==temp):
#     print(temp," is a palindrom number.")
# else:
# #     print(temp," is not a palindrom number.") 
# a=str(input("enter the number:"))
# x=a[::-1]

# if(a==x):
#     print("yes")
