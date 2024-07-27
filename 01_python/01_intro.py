print("hello world" ,5)
print(5*10)
print("    Your poem here   ")

# use for single comment shortcut: ctrl+ "/" 

'''multiple 
line 
comment'''

#or

"""multiple 
line 
comment"""

# print("My name is:
#       premansu chakraborty") #this is not the right thing for new line

print("My name is: \n premansu chakraborty") # we use '\n' for new line

#Escape Sequence Characters "\"

# print("My name is: "Premansu Chakraborty"")  #throws error because python interpreter got confuced 
# To insert characters that cannot be directly used in a string, we use an escape sequence character.
# An escape sequence character is a backslash \ followed by the character you want to insert.
print("My name is: \"Premansu Chakraborty\"") #output:My name is: "Premansu Chakraborty"
 
"""
 The syntax of a print statement looks something like this:

print(object(s), sep="separator", end="end", file=file, flush=flush)

Other Parameters of Print Statement
object(s): Any object, and as many as you like. Will be converted to string before printed
sep='separator': Specify how to separate the objects, if there is more than one. Default is ' '
end='end': Specify what to print at the end. Default is '\n' (line feed)
file: An object with a write method. Default is sys.stdout
Parameters 2 to 4 are optional"""

print("hello","everyone",sep="##",end="007") #output:hello##everyone007
