#prgm to replace a word 'this' with 'that' and display th sentence
s=input("enter the sentences : ")
# s.replace("this","that")
l=s.split( )
# print(l)
leng = len(l)
for i in range(0,leng):
    if(l[i]=="this"):
        l[i]="that"

print(l)