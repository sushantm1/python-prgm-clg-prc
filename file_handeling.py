# prgm to replace "this" with that in a txt file. 
with open("Student.txt","r") as file:
    data=file.read()
    print("-->this is the data in initial file below.")
    print(data)
    new_data=data.replace("this","that")
    print("-->data completly updated(\"this\" is replaced by \"that\").")
    print(new_data)
with open("Student.txt","w") as file:
    file.write(new_data)
    print("updation complete.")