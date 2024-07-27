'''String formatting in python
String formatting can be done in python using the format method.

txt = "For only {price:.2f} dollars!"
print(txt.format(price = 49))


f-strings in python
It is a new string formatting mechanism introduced by the PEP 498. It is also known as Literal String Interpolation or more commonly as F-strings (f character preceding the string literal). The primary focus of this mechanism is to make the interpolation easier.

When we prefix the string with the letter 'f', the string becomes the f-string itself. The f-string can be formatted in much same as the str.format() method. The f-string offers a convenient way to embed Python expression inside string literals for formatting.

Example
val = 'Geeks'  
print(f"{val}for{val} is a portal for {val}.")  
name = 'Tushar'  
age = 23  
print(f"Hello, My name is {name} and I'm {age} years old.")


Output:
Hello, My name is Tushar and I'm 23 years old.


In the above code, we have used the f-string to format the string. It evaluates at runtime; we can put all valid Python expressions in them.

We can use it in a single statement as well.

Example
print(f"{2 * 30})"


Output:
60'''

#string formating

choice='tea'
price=87.02365
order='customer wants {} and the price of {} is {}'
print(order.format(choice,choice,price)) #by using this we can add variables in string
#another way to do that 
order2='customer wants {0} and the price of {0} is {1}'
print(order2.format(choice,price)) 

cost='the price of {0} is {1:.2f}' #take price as two decimal places
print(cost.format(choice,price))

# another example
# txt = "For only {price:.2f} dollars!"
# print(txt.format(price = 49))

#f string is the easier version of string formating-->we can easily pass the var.

order3=f'customer wants {choice} and the price of {choice} is {price}'
print(order3)

cost=f'the price of {choice} is {price:.2f}' #take price as two decimal places
print(cost) 

#we can calculate some values at runtime but the return type of output wiil be string
print(type(f"{2 * price}"))
print(f"{2 * price}")


#f-string cancelation
order3=f'customer wants {{choice}} and the price of {{choice}} is {{price}}'
print(order3)
cost=f'the price of {{choice}} is {{price:.2f}}' 
print(cost) 
