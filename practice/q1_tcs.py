# prgm to take integer input from user and store it in array
# import array as arr
import numpy
from astropy.io.fits import append
from num2words import num2words
# def num2words() as N2W

# function
def


# function to find largest num and updating the temp_num_list
def largest_num():
    global temp_num_list, main_list
    temp_list=[]
    large_num = 0
    length=len(temp_num_list)
    for i in range(j, length):
        if large_num < temp_num_list[i]:
            large_num = temp_num_list[i]
        temp_list.append(i)
        temp_num_list.pop(i)
    # main_list.append(temp_list)
    return large_num




# mian prgm
arr_size=int(input("enter the array size : "))
num_list=[]
for i in range(0,arr_size):
    x=int(input("enter the array element : "))
    num_list.append(x)
print("the list you entered is :", num_list)
alfa_num=[]
for i in num_list:
    x=num2words(i)
    alfa_num.append(x)
print("alphabetic form of the above list is : \n",alfa_num)
vowels="aeiou"
d=0

for i in range(0,arr_size):
    count = 0
    for j in alfa_num[i] :
        if j=='a':
            count=count+1
        if j=='e':
            count=count+1
        if j=='i':
            count=count+1
        if j=='o':
            count=count+1
        if j=='u':
            count=count+1

    d=d+count
print("total numbers of vowels are : ",d)

temp_num_list=num_list

# len=len(temp_num_list)
temp1=d//2
temp2=temp1
totalsum=d
main_list=[]
remain_num=0






# my approach
# for j in range(0,arr_size):
#     temp_list=[]
#     for i in range(j,arr_size):
#         if temp1<num_list[i]:
#             sum= sum + int(num_list[i])
#             temp_list.append(i)
#         if totalsum==sum :
#             break
#         temp2=temp2//2
#     main_list.append(temp_list)

print("the total number of combinations are in the list below :")
print(main_list)



# print(num_list)
# print(arr)













# func to number names
# def switch(a):
#     num_name_ones = {
#         1: "one",2: "two",3: "three",4: "four",5: "five",6: "six",7: "seven",8: "eight",9: "nine",10: "ten"
#     }
#     num_names_11to19= {11: "eleven",12: "twelve",13: "thirteen",14: "fourteen",15: "fifteen",16: "sixteen",17: "seventeen",
#                        18: "eighteen",19: "nineteen"
#     }
#     num_name_tens = {20: "twenty",30: "thirty",40: "forty",50: "fifty",60: "sixty",70: "seventy",80: "eighty",
#                      90: "ninety",100: "hundred"
#     }
