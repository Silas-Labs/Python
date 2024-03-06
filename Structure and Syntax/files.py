#file in same directory as the py file

#r(read),w(write),a(append),r+(r+w)

employee_file = open("files.txt","r")
print(employee_file.readable())
#print(employee_file.readlines())

#Use for loop
print("Using For Loop")
for employee in employee_file.readlines():
    print(employee)

#always close file after.
employee_file.close()


# To append, change mode to a!!
print("Append")
employee_file = open("files.txt","a")
employee_file.write("\nKelly - Customer Service")
employee_file.close()

# To Overwrite, change mode to W!!
print("Overwrite")
employee_file = open("files1.txt","w")#You can create a new file here
employee_file.write("\nKelly - Customer Service")
employee_file.close()
