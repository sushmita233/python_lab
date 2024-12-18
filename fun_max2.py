##Q.2) WAP to find maximum among two numbers
def find_max(n1,n2):    
    if n1>= n2: #condition 
        print("first number maximum among two numbers ")
    else:
        print("Second number maximum among two numbers")
    
# input from user
n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))
find_max(n1,n2) # calling function 
