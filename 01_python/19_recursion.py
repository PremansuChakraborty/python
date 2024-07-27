'''Recursion in python
Recursion is the process of defining something in terms of itself.

Python Recursive Function
In Python, we know that a function can call other functions. It is even possible for the function to call itself. These types of construct are termed as recursive functions.

Example:
def factorial(num): 
    if (num == 1 or num == 0):
        return 1
    else:
        return (num * factorial(num - 1)) 
  
# Driver Code 
num = 7; 
print("Number: ",num)
print("Factorial: ",factorial(num))


Output:
number:  7
Factorial:  5040'''

#example

def factorial(num):
    if(num>0):
        return num*factorial(num-1)
    else:
        return 1
    
print(factorial(5))

#example 2

'''# Quick Quiz: Write a program to print the Fibonacci sequence
# f(0) = 0
# f(1) = 1
# f(2) = f(1) + f(0)
# f(n) = f(n-1) + f(n-2)

# 0 1 1 2 3 5 8....'''

def fibonacci(num):
    if(num>1):
        return fibonacci(num-1)+fibonacci(num-2)
    elif(num==1):
        return 1
    else:
        return 0
    
print(fibonacci(6))