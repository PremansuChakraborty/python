'''Python Sets
Sets are unordered collection of data items. They store multiple items in a single variable. Set items are separated by commas and enclosed within curly brackets {}. Sets are unchangeable, meaning you cannot change items of the set once created. Sets do not contain duplicate items.

Example:
info = {"Carla", 19, False, 5.9, 19}
print(info)


Output:
{False, 19, 5.9, 'Carla'}


Here we see that the items of set occur in random order and hence they cannot be accessed using index numbers. Also sets do not allow duplicate values.

Quick Quiz: Try to create an empty set. Check using the type() function whether the type of your variable is a set

Accessing set items:
Using a For loop
You can access items of set using a for loop.

Example:
info = {"Carla", 19, False, 5.9}
for item in info:
    print(item)


Output:
False
Carla
19
5.9'''

# set and dictionary both represented in {}
# but set is unordered collection --> means if we traverse the set we get same values but in different order
# set does not cotain repeated values

info = {"Carla", 19, False, 5.9, 19,5.9}
print(info) #{'Carla', False, 19, 5.9} no repeated values and get values in different orders

for value in info:
  print(value)   # get values in unordered form
  
  

prem={} #--> python interpretor take it as empty dictionary 
print(type(prem)) #<class 'dict'>

prem2=set() #-->now it is a empty set. first bracket imp.
print(type(prem2)) #<class 'set'>

