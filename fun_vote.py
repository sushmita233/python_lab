#Q.3) WAP to check whether a person can vote or not using function
def can_vote(age):
    if age>=18:
        print("You can vote.")
    else:
        print("You cannot vote.")
    
#input from user
age = int(input("Enter your age: "))
can_vote(age)
