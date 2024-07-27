'''What are strings?
In python, anything that you enclose between single or double quotation marks is considered a string. A string is essentially a sequence or array of textual data. Strings are used when working with Unicode characters.

Example
name = "Harry"
print("Hello, " + name)


Output
Hello, Harry

Note: It does not matter whether you enclose your strings in single or double quotes, the output remains the same.

Sometimes, the user might need to put quotation marks in between the strings. Example, consider the sentence: He said, “I want to eat an apple”.

How will you print this statement in python?: He said, "I want to eat an apple". We will definitely use single quotes for our convenience

print('He said, "I want to eat an apple".')


Multiline Strings
If our string has multiple lines, we can create them like this:

a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)


Accessing Characters of a String
In Python, string is like an array of characters. We can access parts of string by using its index which starts from 0.
Square brackets can be used to access elements of the string.

print(name[0])
print(name[1])


Looping through the string
We can loop through strings using a for loop like this:

for character in name:
    print(character)


Above code prints all the characters in the string name one by one!'''

# print : He said, "I want to eat an apple".
# process 1
print("He said, \"I want to eat an apple\".")
# process 2
print('He said, "I want to eat an apple".')




# Multiline Strings
# If our string has multiple lines, we can create them like this:

'''a = "Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."
print(a) #error'''

#Right process
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)


#string as an array

name="Prem"

print(name[0]) #P
print(name[1]) #r

for character in name:
    print(character)
    
    
    
    
"""                           String Slicing & Operations on String
Length of a String
We can find the length of a string using len() function.

Example:
fruit = "Mango"
len1 = len(fruit)  #length of the string= 5
print("Mango is a", len1, "letter word.")

# print(fruit[0:4]) # including 0 to 3 but not 4
# print(fruit[1:4]) # including 1 to 3 but not 4
# print(fruit[:5])  # including 0 to 4 but not 5
# print(fruit[0:-3]) # including 0 to len(fruit)-3=2
# print(fruit[:len(fruit)-3]) # same as print(fruit[0:-3])
#print(fruit[-1:len(fruit) - 3]) # including len(fruit)-1 = 4 to len(fruit)-3=2 # do not make scence so no output 
#print(fruit[-3:-1])  # including len(fruit)-3 = 2 to len(fruit)-1=4
#print(fruit[3])	#returns character at specified index = g
Output:
Mango is a 5 letter word.

String as an array
A string is essentially a sequence of characters also called an array. Thus we can access the elements of this array.

Example:
pie = "ApplePie"
print(pie[:5])
print(pie[6])	#returns character at specified index


Output:
Apple
i


Note: This method of specifying the start and end index to specify a part of a string is called slicing.

Slicing Example:
pie = "ApplePie"
print(pie[:5])      #Slicing from Start
print(pie[5:])      #Slicing till End
print(pie[2:6])     #Slicing in between
print(pie[-8:])     #Slicing using negative index


Output:
Apple
Pie
pleP
ApplePie


Loop through a String:
Strings are arrays and arrays are iterable. Thus we can loop through strings.

Example:
alphabets = "ABCDE"
for i in alphabets:
    print(i)


Output:
A
B
C
D
E"""

fruit = "Mango"
print(len(fruit))

print(fruit[0:4]) # including 0 to 3 but not 4
print(fruit[1:4]) # including 1 to 3 but not 4
print(fruit[:5])  # including 0 to 4 but not 5
print(fruit[0:-3]) # including 0 to len(fruit)-3=2
print(fruit[:len(fruit)-3]) # same as print(fruit[0:-3])
print(fruit[-1:len(fruit) - 3]) # including len(fruit)-1 = 4 to len(fruit)-3=2 # do not make scence so no output 
print(fruit[-3:-1])  # including len(fruit)-3 = 2 to len(fruit)-1=4
print(fruit[3])	#returns character at specified index = g

for i in fruit:
    print(i)