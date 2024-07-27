'''List Methods
list.sort()
This method sorts the list in ascending order. The original list is updated

Example 1:
colors = ["voilet", "indigo", "blue", "green"]
colors.sort()
print(colors)
num = [4,2,5,3,6,1,2,1,2,8,9,7]
num.sort()
print(num)


Output:
['blue', 'green', 'indigo', 'voilet']\
[1, 1, 2, 2, 2, 3, 4, 5, 6, 7, 8, 9]


What if you want to print the list in descending order?
We must give reverse=True as a parameter in the sort method.

Example:
colors = ["voilet", "indigo", "blue", "green"]
colors.sort(reverse=True)
print(colors)
num = [4,2,5,3,6,1,2,1,2,8,9,7]
num.sort(reverse=True)
print(num)


Output:
['voilet', 'indigo', 'green', 'blue']
[9, 8, 7, 6, 5, 4, 3, 2, 2, 2, 1, 1]


The reverse parameter is set to False by default.

Note: Do not mistake the reverse parameter with the reverse method.

reverse()
This method reverses the order of the list.

Example:
colors = ["voilet", "indigo", "blue", "green"]
colors.reverse()
print(colors)
num = [4,2,5,3,6,1,2,1,2,8,9,7]
num.reverse()
print(num)


Output:
['green', 'blue', 'indigo', 'voilet']
[7, 9, 8, 2, 1, 2, 1, 6, 3, 5, 2, 4]


index()
This method returns the index of the first occurrence of the list item.

Example:
colors = ["voilet", "green", "indigo", "blue", "green"]
print(colors.index("green"))
num = [4,2,5,3,6,1,2,1,3,2,8,9,7]
print(num.index(3))


Output:

1
3


count()
Returns the count of the number of items with the given value.

Example:
colors = ["voilet", "green", "indigo", "blue", "green"]
print(colors.count("green"))
num = [4,2,5,3,6,1,2,1,3,2,8,9,7]


Output:
2
3


copy()
Returns copy of the list. This can be done to perform operations on the list without modifying the original list.

Example:
colors = ["voilet", "green", "indigo", "blue"]
newlist = colors.copy()
print(colors)
print(newlist)


Output:
['voilet', 'green', 'indigo', 'blue']
['voilet', 'green', 'indigo', 'blue']


append():
This method appends items to the end of the existing list.

Example:
colors = ["voilet", "indigo", "blue"]
colors.append("green")
print(colors)


Output:
['voilet', 'indigo', 'blue', 'green']


insert():
This method inserts an item at the given index. User has to specify index and the item to be inserted within the insert() method.

Example:
colors = ["voilet", "indigo", "blue"]
#           [0]        [1]      [2]
colors.insert(1, "green")   #inserts item at index 1
# updated list: colors = ["voilet", "green", "indigo", "blue"]
#       indexs              [0]       [1]       [2]      [3]
print(colors)


Output:
['voilet', 'green', 'indigo', 'blue']


extend():
This method adds an entire list or any other collection datatype (set, tuple, dictionary) to the existing list.

Example 1:
#add a list to a list
colors = ["voilet", "indigo", "blue"]
rainbow = ["green", "yellow", "orange", "red"]
colors.extend(rainbow)
print(colors)


Output:
['voilet', 'indigo', 'blue', 'green', 'yellow', 'orange', 'red']


Concatenating two lists:
You can simply concatenate two lists to join two lists.

Example:
colors = ["voilet", "indigo", "blue", "green"]
colors2 = ["yellow", "orange", "red"]
print(colors + colors2)


Output:
['voilet', 'indigo', 'blue', 'green', 'yellow', 'orange', 'red']


'''


lisst=[23,54,52,20,55,60,30,100,12,63,41]
lisst.sort() #accending order
print(lisst)
lisst.sort(reverse=True) #decending order
print(lisst)
print("end".center(75,"."))

list1=[23,54,52,20,55,60,30,100,12,63,41]
list1.reverse()
print(list1)
print("end".center(75,"."))

colors = ["voilet", "green", "indigo", "blue", "green"]
print(colors.index("blue"))
print(colors.index('green'))
print("end".center(75,"."))

colors = ["voilet", "green", "indigo", "blue", "green"]
print(colors.count("green"))
print("end".center(75,"."))

# list2=list1 #means nor copying the values from list1 to list2 it means create a instance of list 1 in the name of list2 that means any changes in list1 reflected list2. in the memory address is same for both
# #so to avoid that problem we use copy function
list2=lisst.copy()
print(list2)
print("end".center(75,"."))

# add any thing in the end of the list
list2.append(55) #we can add only one element
print(list2)
print("end".center(75,"."))

#remove one element
list2.pop(3) #index 3 element will poped
print(list2)
print("end pop".center(75,"."))

#enter any thing at any position/index

list2.insert(2,"prem")
list2.insert(6,"Souvik")
list2.insert(10,"mahi")
print(list2)
print("end".center(75,"."))

#add two lists a.extend(b)--> means add all the ele of b in the end of a
list3 = ["voilet", "indigo", "blue"]
list3.extend(list2)
print(list3)
print("end".center(75,"."))

#else

colors = ["voilet", "indigo", "blue", "green"]
colors2 = ["yellow", "orange", "red"]
colors3=colors + colors2
print(colors3)