# Python Program to Concatenate Two Dictionaries Into One
d1={'sushant':12,'Rohan':56}
d2={'akash':985,'viaksh':965}
d3={}
# by using loops
for key, value in d1.items():
    d3[key]=value
for key, value in d2.items():
    d3[key]=value
# by using "|" operator
c=d1|d2
print(c)
# print(d3)