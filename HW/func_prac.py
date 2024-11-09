#prgm to define different functions

#fun() to find HCF of a number
def hcf(n1,n2):
    small= n1 if n1<n2 else n2
    # print(small)
    # rem=small//2
    for i in range(small,2,-1):
        if n1%i==0 and n2%i==0:
            return(i," is the HCF of ",n1," and ",n2)
    else:
        return ("HCF not found.")

#fun() to return sum of n integers
def n_sum(n):
    sum=n*(n+1)/2
    return int(sum)

#fun() to check greatest number among three
def great_num(n1,n2,n3):
    if n3<n1>n2:
        return (n1," is the greatest number.")
    elif n3<n2>n1:
        return (n2," is the greatest number.")
    else:
        return (n3," is the greatest number.")

# fun() to check a number i sprime or not
def isprime(x):
    rem=x//2
    for i in range(2,rem):
        if x%i==0:
            return ("it's not a prime number.")
    else:
        return ("it's a prime number.")

# fun() to check a number is palindrom or not;
def palindrom(s):
    d=s[::-1]
    if(s==d):
        return "it's a palindrom number."
    else:
        return "it's not a palindrom number."

# main
s1=int(input("enter the first number :"))
s2=int(input("enter the second number :"))
# s3=int(input("enter the third number :"))

# print(palindrom(s))
# print(isprime(s))
# print(n_sum(s1))
print(hcf(s1,s2))
