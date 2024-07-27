'''Python - else in Loop
As you have learned before, the else clause is used along with the if statement.

Python allows the else keyword to be used with the for and while loops too. The else block appears after the body of the loop. The statements in the else block will be executed after all iterations are completed. The program exits the loop only after the else block is executed.

Syntax
for counter in sequence:
    #Statements inside for loop block
else:
    #Statements inside else block


Example:
for x in range(5):
    print ("iteration no {} in for loop".format(x+1))
else:
    print ("else block in loop")
print ("Out of loop")


Output:
iteration no 1 in for loop
iteration no 2 in for loop
iteration no 3 in for loop
iteration no 4 in for loop
iteration no 5 in for loop
else block in loop
Out of loop'''

#else is the part of the loop, when the loop content is complete to execute then the else is executed.
#else will execute   
for i in [1,5,6,3,1,3,2]:
    print(i)

else:
    print("control is out of the loop")    
#output
'''1
5
6
3
1
3
2
control is out of the loop'''
print("".center(50,"."))  
#but if the loop is breaked then else is not executed. remember else is the last part of the loop but if loop is breaked then else is not worked.
#else will not execute   
for i in range(6):
    print(i)
    if i==4:
        break

else:
    print("control is out of the loop")  
    
print("".center(50,"."))  
#output
'''0
1
2
3
4'''


#else with while loop
#else will execute
i=6

while i>0:
    print(i)
    i=i-1
else:
    print("control is out of the loop")  
    

print("".center(50,"."))   
#else will not execute   
i=6

while i>0:
    print(i)
    i=i-1
    if i<2:
        break
else:
    print("control is out of the loop")  