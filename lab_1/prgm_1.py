# #prgm to 
# a=int(input("enter a number : "))
# temp=a
# temp2=0
# while(a>0):
#     remainder=a%10
#     temp2=temp2+remainder
#     a=a//10

# print("sum of it's digit : ",temp2)

s=str(input("enter the nember"))
sum=0
for i in s:
    sum+=int(i)
print(sum)