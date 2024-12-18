#Q.1)Create dynamic list where you will ask user to enter 5 elements in it and perform insert new element and delete an element operation on it.
mylist = []

# Accept 5 elements from users
for i in range(5):
    nums= int(input("Enter numbers: "))
    mylist.append(nums)

print("List:", mylist)
print("-----------------------")

# Insert a new element
no_add = int(input("Enter an element to insert: "))
mylist.append(no_add)  # Insert at the end
print("List after inserting:", mylist)
print("-----------------------")

# Delete an element
no_del = int(input("Enter an element to delete: "))
if no_del in mylist:
    mylist.remove(no_del)
    
else:
    print("Element not found!")
print("List after deletion:", mylist)
print("-----------------------")
