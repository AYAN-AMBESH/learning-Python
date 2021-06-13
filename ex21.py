# Write a Python program to test whether a passed letter is a vowel or not
l = input("ENTER A LETTER: ")
list= ['a','A','e','E','i','I','o','O','u','U']
if l in list:
    print("The inputted letter is a vowel")
else:
    print("The inputted letter is not a vowel")