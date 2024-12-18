#WAP to get the table of a number using function
#define function
def multi_table(n):
    for a in range(1,11): # 10 times
        print(n," × ",a," = ",(n*a))

# input from user
num = int(input("Enter a number : "))
multi_table(num)#calling function
