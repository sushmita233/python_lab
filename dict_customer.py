###WAP to create dictionaries for below task and perform all the above operations on it.
###Each customer ID in a company is associated with a customer name.
##
### Creating a dictionary 
##dict_cust = {101:"Rajiv",102:"Santosh",103:"soham"}
##
##print("Customer in company",dict_cust)
##
###Add new Customer
##add_id = int(input("Enter new customer id: "))
##add_cust = input("Enter new customer name: ")
##dict_cust[add_id] = add_cust
##print("New customer added successfully.")
###print output
##print("Customer in company",dict_cust)
##print("-------------------------")
##
##
###Update Customer
##up_id =int( input("Enter id to update: "))
##if up_id  in dict_cust:
##    custName= input("Enter new Customer name: ")
##    dict_cust[up_id] =custName
##    print("updated successfully......")
##else:
##    print("Customer not found")
###print output
##print(" Customer in company :",dict_cust)
##print("-------------------------")
##
###Remove Customer
##if dict_cust:
##    remove_id =int( input("Enter the customer id to remove: "))
##    if remove_id  in dict_cust:
##        removed_name = dict_cust.pop(remove_id)
##        print("Removed successfully......")
##        print("Removed Customer id:", remove_id )
##        print("Removed Customer: ",removed_name)
##        #print output
##        print("Custome record in company :",dict_cust)
##    else:
##        print("Customer not found.")
##else:
##    print("No Customer available to remove.")
##print("-------------------------")
##
###Print all items present company
##print("Print all items present company.")
##for i in dict_cust.items():
##    print(i)
##print("-------------------------")
##
###Print only  customer id.
##print("Print only customer id.")
##for i in dict_cust.keys():
##    print(i)
##print("-------------------------")
##
##
###Print only customer name
##print("Print only customer name.")
##for i in dict_cust.values():
##    print(i)
##print("-------------------------")

my_set = set()
my_set.add(10)
my_set.add(20)
my_set.clear()
print(my_set)





my_set = {1, 2, 3, 4, 5}

my_set.add(3)
print(my_set)











