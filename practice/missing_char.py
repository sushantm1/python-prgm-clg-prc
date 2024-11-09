# import py
import re
import string
s="7985interdisciplinary12"
digits = "0123456789"
# n=[int(word) for word in s.split() if word.isdigit]
n=re.findall(r'\d+', s)
a=re.findall(r'\D+', s)
nl=[]
al=[]
for i in n:
    nl.append(i)
for i in a:
    al.append(i)

print(nl)
print(al)
fnl=[]
alphabets = string.ascii_lowercase
for i in digits:
    if i not in ''.join(n):
        fnl.append(i)
for i in alphabets:
    if i not in s:
        fnl.append(i)
# for i in fnl:
    # print(fnl,end='')
x=''.join(fnl)
print(x)