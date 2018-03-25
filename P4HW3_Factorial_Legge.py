#CTI-110
#P4HW3: Factorial
#Bradley Legge
#3/25/2018

print("Enter a nonnegative integer: ")
num = int(input())
fact = 1

for i in range(1, num + 1):
    fact = fact * i

print("The factorial of ", num, "is: ", fact)
