#Q.1) WAP to get factorial of a number using function
#define function
def fact(n):
    if n < 0:
        return "Factorial is not for negative numbers."
    elif n == 0:
        return 1
    else:
        result = 1
        for i in range(1, n + 1):
            result=result* i
        return result

num = int(input("Enter a number: "))#input from user
print(f"factorial :" ,fact(num))#calling function
