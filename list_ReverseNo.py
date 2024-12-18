#Q.2)WAP to reverse the element in List 
mylist = input("Enter elements separated by spaces: ").replace(",", " ").split()
print("Original List:", mylist)

# Reverse the list
mylist = mylist[::-1]
print("Reversed List:", mylist)
