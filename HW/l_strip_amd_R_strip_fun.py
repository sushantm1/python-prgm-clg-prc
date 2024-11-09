# prgm to check how strip() works ...
# strip() removes a particular word or character from the string
# it also have two types-- 
#                         |--> rstrip(from right side).
#                         |--> lstrip(from lefd side)

d="@thi@s @is an @e@xample@."
# r=
print("replace() to remove a char =",d.replace("@",'')) 
print("strip() to remove a char from first occuring =",d.strip("@")) 
print("lstrip() remove char from left side of a string =",d.lstrip("@")) 
print("rstrip() remove char from eight side of a string =",d.lstrip("@")) 