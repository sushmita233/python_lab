#1.Write a program to find greatest among two numbers
#input of 2 numbers from users
num1=int(input("Enter a number1: "))
num2=int(input("Enter a number2: "))

#Conditions to find the greatest number
if (num1>num2):
    print("Number 1 is the greatest")
    print("Number 2 is the Smallest")
    
elif num2 > num1:
    print("Number 2 is the greatest.")
    print("Number 1 is the Smallest")
    
else:
    print("Both numbers are equal.")

