# user defined exceptions
class MCA_error(Exception):
    pass

try:
    a=int(input("enter the number : "))
    if(a==0):
        raise MCA_error("a is zero")
    b=23/a
    print(b)
finally:
    print("an error occured")

