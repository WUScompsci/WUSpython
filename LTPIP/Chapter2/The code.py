# The Code for all the tasks above

"""Check that your code is correct by comparing it to the code below, but only ONCE YOU HAVE TRIED TO COMPLETE THE TASKS BY YOURSELF"""

# Chapter 2, Example 1 string methods.py
astring = "You've done a good job"
print("Original string:", astring)
print("nUppercase string:", astring.upper())
print("New String:",astring.replace("good","brilliant"))
print("Original string:",astring)
print("The word 'done' starts at index",astring.index("done"))
input ("\nPress Enter to exit")

# Chapter 2, Example 2 string methods.py
astring = "You've done a good job"
print("\nOriginal string:" astring)
print("\nUppercase string:", astring.upper)
print("\nNew String:",astring.replace("good","excellent")
print("\nOriginal string:",astring)
input ("\nPress Enter to exit")

# Chapter 2, Example 3 Cost of lunch.py
main = 3.00
juice = 0.75
banana = 1.00
total = main + juice + banana
print("Total for lunch: ",total)
input ("\nPress Enter to exit")

# Chapter 2, Example 4 Cost of lunch v2.py
main = input("Enter cost of main course: ")
juice = input("Enter cost of juice: ")
banana = input("Enter cost of banana: ")
total = main + juice + banana
print("Total for lunch: ",total)
input ("\nPress Enter to exit")

# Chapter 2, Example 5 Cost of lunch v3.py
main = float(input("Enter cost of main course: "))
juice = float(input("Enter cost of juice: "))
banana = float(input("Enter cost of banana: "))
total = main + juice + banana
print("Total for lunch: {:.2f}".format(total))
input ("\nPress Enter to exit")

# Chapter 2, Exercise 1 string methods.py
proverb = "A picture's worth a thousand words"
proverbImage = proverb.replace("A picture's","An image is")
print("amended proverb ",proverbImage)
firstO = proverb.find("o")
print("First occurrence of 'o' is at index",firstO)
proverbUpper = proverb.upper()
print("Uppercase string :",proverbUpper)
print("Length of string =",len(proverb))
input ("\nPress Enter to exit")

# Chapter 2, Exercise 2 radius and circumference.py
PI = 3.14159
r = float(input("Enter radius of circle: "))
print("Area is",PI *r**2)
print("Circumference is",2 * PI * r)
input ("\nPress Enter to exit")

# Chapter 2, Exercise 3 rounding floating point numbers.py
num1 = float(input("Please enter your first number: "))
num2 = float(input("Please enter your second number: "))
sum = num1 + num2
roundedSum = round(sum,2)
print("The sum of ", num1,"and ",num2, "is", roundedSum)

#Here is another way of printing the answer to a calculation
product = round(num1 * num2,3)
print("The product of " + str(num1) + " and " + str(num2) + " is " + str(product))     

#  Chapter 2, Exercise 4

rhyme=input("Enter the first line of a nursery rhyme in lower case: ")
print("The length of the string is",len(rhyme))
rhyme=rhyme.upper()
start=int(input("Type a starting number: "))
end=int(input("Type an ending number: "))
print(rhyme[start:end])

#  Chapter 2, Exercise 5
pounds = int(input("How many pounds to you want to convert? "))
euros = pounds * 1.18
print("£",pounds, "is equal to €", euros)

# Or a little bit more useful
pounds = float(input("How many pounds to you want to convert? "))
euros = pounds * 1.18
print("£",pounds, "is equal to €", euros)
fifty = int(euros//50)
left = euros-(fifty*50)
print (fifty, "€50 notes")
twenty = int(left//20)
left = left-(twenty*20)
print (twenty, "€20 notes")
ten = int(left//10)
left = left-(ten*10)
print (ten, "€10 notes")
five = int(left//5)
left = left-(five*5)
print (five, "€5 notes")
print ("This leaves €", left)






                                      
