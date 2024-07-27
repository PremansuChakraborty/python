"""Operators
Python has different types of operators for different operations. To create a calculator we require arithmetic operators.

Arithmetic operators
Operator	Operator Name	Example
+	Addition	15+7
-	Subtraction	15-7
*	Multiplication	5*7
**	Exponential	5**3
/	Division	5/3
%	Modulus	15%7
//	Floor Division	15//7
What is meant by floor division? Floor division is a mathematical operation in Python that divides two numbers and rounds the result down to the nearest integer. The floor division operator // is used for this operation, and it returns an integer result without any decimal places.
"""


print(2**3) #to the power
print(12%5) #modulus
print(126/5) #div
print(126//5) #floor div (roundoff the nearest integer)

# take input using input function val = input("What is your num?\n") *** print(type(val))=<class 'str'>
# input take string value as input
# take input from user
# input_a = input()
 
# # print data type
# print(type(input_a))=<class 'str'>

 
# # type cast into integer
# input_a = int(input_a)
 
# # print data type
# print(type(input_a))=<class 'int'>

#ELSE

# # integer input
# input_b = int(input())
 
# # print type
# print(type(input_b))=<class 'int'>

"""CREATE A CALCULATOR"""
A = int( input("FIRST num: \n"))
B = int(input("second num: \n"))

ope=input("ENTER YOUR OPERATION: For Addition enter +, For substraction enter -,\nFor Multiplication enter *, For Divition enter /, For floor Divition enter //,\nFor Exponente enter **, For Mouduls enter %.\n" )

if ope=="+":
    print(A+B)
elif ope=="-":
    print(A-B)  
elif ope=="*":
    print(A*B) 
elif ope=="/":
    print(A/B)     
elif ope=="//":
    print(A//B)  
elif ope=="**":
    print(A**B)   
elif ope=="%":
    print(A%B) 
else:
    print("WRONG ENTRY TRY AGAIN")    
       