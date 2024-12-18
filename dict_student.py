#WAP to create dictionaries for below task and perform all the above operations on it.
#Each student in a school is associated with their grade.

# Creating a dictionary 
studs_gd = {"Anjali": "A","Raj": "B","Ritika": "C","Disha": "C"}

print("Students in a School",studs_gd)

#Add new Student
add_stud = input("Enter new student's name: ")
add_grade = input("Enter the student's grade: ")
studs_gd[add_stud] = add_grade
print("New student added successfully.")
print("Students in a School",studs_gd)
print("-------------------------")


#Update student
up_stud = input("Enter product name to update: ")
if up_stud in studs_gd:
    grade = input("Enter new grade: ")
    studs_gd[up_stud] = grade
    print("updated successfully......")
else:
    print("Student not found")
print(" student record in school :",studs_gd)
print("-------------------------")

#Remove student
if studs_gd:
    remove_stud = input("Enter the student's name to remove: ")
    if remove_stud in studs_gd:
        removed_grade = studs_gd.pop(remove_stud)
        print("Removed successfully......")
        print("Removed Student:", remove_stud )
        print("Removed Grade: ",removed_grade)
        print(" student record in school :",studs_gd)
    else:
        print("Student not found.")
else:
    print("No students available to remove.")
print("-------------------------")

#Print all items present in School
print("Print all items present in School.")
for i in studs_gd.items():
    print(i)

print("-------------------------")
#Print only Student names.
print("Print only Student names..")
for i in studs_gd.keys():
    print(i)
print("-------------------------")
#Print only grades
print("Print only grades.")
for i in studs_gd.values():
    print(i)
print("-------------------------")















