# 
# Example file for variables
# LinkedIn Learning Python course by Joe Marini
#


# Basic data types in Python: Numbers, Strings, Booleans, Sequences, Dictionaries
myint = 5
myfloat = 13.2
mystr = "This is a string"
mybool = True
mylist = [0, 1, "two", 3.2, False]
mytuple = (0, 1, 2)
mydict = {"one" : 1, "two" : 2}
myarray = (0,2,2)

# print(myint)
# print(myfloat)
# print(mystr)
# print(mybool)
# print(mylist)
# print(mytuple)
# print(mydict)

# re-declaring a variable works
myfloat = 345555
mystr = "This is not a string"
print(mystr)

# to access a member of a sequence type, use []
print(mylist[7])
print(mytuple[5])

# to delete an element of a list use .pop(index)
mylist.append("Yoyo")
print(mylist)



# use slices to get parts of a sequence
print(mylist[0:3:2])
print(mylist)
print(mylist[::-2])

# you can use slices to reverse a sequence

# dictionaries are accessed via keys
print(mydict["one"])

# ERROR: variables of different types cannot be combined
print("This is my number"+ str(myfloat)) #Error
print("This is my number" + str(myfloat)) #Prints output but there is no space
print("This is my number",str(myfloat)) #Prints output with space

# Global vs. local variables in functions
def myFunction():
    global mylist #Keyword global enables access to the global variable mylist
    mylist = [1,3,4,55]
    print(mylist)

myFunction()
print(mylist) 
