'''Exception Handling
Exception handling is the process of responding to unwanted or unexpected events when a computer program runs. Exception handling deals with these events to avoid the program or system crashing, and without this process, exceptions would disrupt the normal operation of a program.

Exceptions in Python
Python has many built-in exceptions that are raised when your program encounters an error (something in the program goes wrong).

When these exceptions occur, the Python interpreter stops the current process and passes it to the calling process until it is handled. If not handled, the program will crash.

Python try...except
try….. except blocks are used in python to handle errors and exceptions. The code in try block runs when there is no error. If the try block catches the error, then the except block is executed.

Syntax:
try:
     #statements which could generate 
     #exception
except:
     #Soloution of generated exception


Example:
try:
    num = int(input("Enter an integer: "))
except ValueError:
    print("Number entered is not an integer.")


Output:
Enter an integer: 6.022
Number entered is not an integer.'''


#we are using try and except to handel the error

num=int(input("enter the num:"))
list1=[12,6,3,6,4,6,3,2]

print(list1[num])
print("".center(50,"."))
#if num is not an int then we get a ValueError
#and if num>7 then we get IndexError

#to handel this errors we use try and except.
#enter an invalid input like str or >7
try:
    num=int(input("enter the num:"))
    list1=[12,6,3,6,4,6,3,2]
    print(list1[num])
except:
    print("error occured")
    
print("".center(50,"."))


#we can handel different type of error as well

try:
    num=int(input("enter the num:"))
    list1=[12,6,3,6,4,6,3,2]
    print(list1[num])
except ValueError: #in case of wrong data type input like:uwgiuf
    print("ValueError occured")
except IndexError: #in case of index exceed problem input like:8/9/10(>7)
    print("IndexError occured")
print("".center(50,"."))    
#why we need to handel error?
'''error stop the execution of the rest code, and the rest code did not executed. by handeling this errors we make sure that total code execute properly'''

#like: this code has an index error, so line 4,5,6 is not going to execute
'''num=10
list1=[12,6,3,6,4,6,3,2]
print(list1[num])
print("this is a error handeling code.")
print("THE END!!!")
print("".center(50,"."))'''

# but if we handel this code then the rest code will run smoothly
try:
    num=10
    list1=[12,6,3,6,4,6,3,2]
    print(list1[num])
except:
    print("ERROR OCCURED")
print("this is a error handeling code.")
print("THE END!!!")
print("".center(50,"."))
