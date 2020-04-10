# Chapter 2, Exercise 3 rounding floating point numbers

# Write a program which asks the user to type in two floating point
# numbers named num1  and num2. Then the program rounds and prints their
# sum and product to the specified number of decimal places.
# The function to round a number 2 decimal places is
# roundedNumber = round(number,2)

num1 = ________(input("Please enter your first number: "))
num2 = ________(input("Please enter your second number: "))
sum = _________ + ____________

# Function to round the sum of the 2 variables off to the nearest 2 decimals
roundedSum = __________(______,2)

print("The sum of ", ______,"and ",_______, "is", ________________)

#Here is a second way of printing the answer to a calculation
#The numbers have been converted to strings so the + sign can be used
#to concatenate the parts of the sentence, and
#the answer has been rounded to three decimal places

product = round(num1 * num2,3)

print("The product of " + str(num1) + " and " + str(num2) + " is " + str(product))    
