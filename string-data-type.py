# defines variable "myString#
myString = "This is a string."
# display variable "myString"
print(myString)
# display variable "myString" with datatype
print(type(myString))
#Displays "you like a" with the two variables listed after
print(myString + " is of the data type " + str(type(myString)))
#defines "firststring" variable as water
firstString = "water"
#defines "secondstring" variable as fall
secondString = "fall"
#defines the "thirdstring" variable as the concat of the two previous variables 
thirdString = firstString + secondString
#Displays the result of the concat 
print(thirdString)
#Asks use to imput their name and asigns it to "name" variable
name = input("What is your name? ")
#Displays Name Variable 
print(name)
#Asks use to imput their favorite color and asigns it to "color" variable
color = input("What is your favorite color?  ")
#Asks use to imput their favorite animal and asigns it to "name" variable
animal = input("What is your favorite animal?  ")
#Displays " NAME you like a" with the two variables listed after, using {} as placeholders
print("{}, you like a {} {}!".format(name,color,animal))