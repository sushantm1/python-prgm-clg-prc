f=open("Student.txt","r")
d=f.read()
print(d)
l=d.split()
print(l)
length=len(l)
print(length)
# t="my name is sushant"
   #"new line in the list"]
# f.write(t)
# f.write("\nthis is a new line")
print("done")
f.close()

#q2 count this in the file
f=open("Student.txt","r")
d=f.read()
l=d.split()
count=0
for i in l:
    if i=="this":
        count=count+1
print("no. of this is :",count)
f.close()

# replacing this with that
f=open("Student.txt","r+")
data=f.read()
len=len(data)

for i in l:
    if i=="this":
        i="that"
f.write(' '.join(l))
f.close()
