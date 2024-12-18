#WAP to create dictionaries for below task and perform all the above operations on it.
#Each product in a supermarket is associated with its price.

# Creating a dictionary 
dict_prod = {"Apple": 50,"Banana": 20,"Orange": 30,"Bread": 35}

print("Products in a Supermarket:",dict_prod)

#Add new product
add_prod=input("Enter new Product: ")
add_price=int(input("Enter price: "))
dict_prod[add_prod] = add_price
print("New Product added successfully.....")
print("New Products add in a Supermarket:",dict_prod)

print("-------------------------")

#Update Product
up_prod = input("Enter product name to update: ")
if up_prod in dict_prod:
    price = int(input("Enter new price: "))
    dict_prod[up_prod] = price
    print("updated successfully......")
else:
    print("Product not found")
print("Updated Products in a Supermarket:",dict_prod)
print("-------------------------")

#Remove Product
if dict_prod  :
    remove_prod = input("Enter the Product's name to remove: ")
    if remove_prod in dict_prod:
        removed_price = dict_prod .pop(remove_prod)
        print("Removed successfully......")
        print("Removed product:", remove_prod )
        print("Removed Price: ",removed_price)
        print("Products in a Supermarket:",dict_prod)
    else:
        print("Product not found.")
else:
    print("No products available to remove.")
print("-------------------------")

#Print all items present in Supermarket
print("Print all items present in Supermarket")
for i in dict_prod.items():
    print(i)

print("-------------------------")
#Print only Product names.
print("Print only Product names.")
for i in dict_prod.keys():
    print(i)
print("-------------------------")
#Print only product price
print("Print only product price.")
for i in dict_prod.values():
    print(i)
print("-------------------------")









