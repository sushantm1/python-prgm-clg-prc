# #prgm to display sum of odd values of the series ex: 2 3 6 8 9 sum = 12

# s=str(input("enter the series :"))
# a=int(s)
# print(a)
# sum=0
# while(a>0):
#     temp=a%10
#     if(temp%2!=0):
#         sum= sum + temp
#     a=a//10

# print(sum)

s=str(input("enter the series : "))
l=s.split( )
print(l)
sum=0
for i in l:
    if(int(i)%2!=0):
        sum=sum+ int(i)

print(sum)