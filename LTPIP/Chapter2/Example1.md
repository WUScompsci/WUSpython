# Chapter 2:  String methods

Python uses ‘methods’ -  a method is written using the 'dot' notation, 
Example:   the string.upper(firstName)
1) the name of the object on the left, followed by a full-stop (eg. string.  )
2) then the method name, followed by parentheses(____)  (eg.   .upper()  )
3) then in parentheses the object (often a variable) the method is applied to (eg.  (firstName)

### Reminder!! 
A method is a function that “belongs to” an 'object'. An object consists of data and/or behaviour.
A method defines a particular behaviour of the object.  

In the examples below ‘string’ and 'firstName' are just the name of the objects, like:
### string.upper(___)	  string.lower(___)      firstName.lower(___)     string.find(___)  
### string.replace(____)   firstName.replace(____)   astring.index(_____)

### Replace the _______ bits with the correct code.  The code below also has syntax errors.  

### Once you've changed it, copy the 'Raw' code and then run it in the Main window of repl.it

astring = "You've done a good job"
print("Original string:", astring)

print("nUppercase string:", astring.________())
print("To replace the string 'good' with a new string:",astring.__________("good","brilliant"))
print("The new string is:",astring)

print("The first occurence of 'v' is at index :",astring.__________('v'))
print("The word 'done' starts at index",astring.____________("done"))

input ("\nPress Enter to exit")

