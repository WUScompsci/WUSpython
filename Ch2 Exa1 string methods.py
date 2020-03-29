# -*- coding: cp1252 -*-
#Program name: Ch 2 Example 1 string methods.py
#Tests string methods
#Python uses ‘methods’ -  a method is written using the 'dot' notation,
# example:    string.upper(___)
# the name of the object on the left, followed by a full-stop
# then the method name, followed by parentheses(____)

# A method is a function that “belongs to” an 'object'. An object consists of data
# and/or behaviour. A method defines a particular behaviour of the object.  
# In the examples below ‘string’ and 'firstName' are just the name of the objects (variables):
#   string.upper(___)	     string.lower(___)      firstName.lower(___)
#   string.find(___)         string.replace(____)   firstName.replace(____)


astring = "You've done a good job"
print("Original string:", astring)
print("nUppercase string:", astring.upper())
print("New String:",astring.replace("good","brilliant"))
print("Original string:",astring)
print("The word 'done' starts at index",astring.index("done"))

input ("\nPress Enter to exit")


                                      
                                      
