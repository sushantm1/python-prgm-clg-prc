#prgm to check a number is prime or not
a=int(input("enter a number : "))
i=2
c=a//2
while(i<=c):
    if(a%i==0):
        print(a,"is not a prime number.")
    i+=1
else:
    print(a,"it's a prime number.")