#prgm to find th e number of digit present in a number
num=int(input())
i=0
while(num!=0):
    num=num//10
    i=i+1
print(i)