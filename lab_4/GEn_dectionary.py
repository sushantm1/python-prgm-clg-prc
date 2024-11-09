# Python Program to Generate a Dictionary that
# Contains Numbers (between 1 and n) in the Form (x,x*x).
n= int(input("enter the number : "))
d={}
sum=0
for i in range(0,n):
    d[i]=i*i
    sum=sum+d[i]
print(d)
print(sum)