x=int(input("Entre the number of employes :"))
D={}
l=[]
for i in range(0,x):
    D["ID"]=int(input("Enter the id of employee no. "  ))
    D["Name"]=str(input("enter the name of teh employee : "))
    D["Salary"]=float(input("enter the salary of employee : "))
    l.append(D) 
print(l)