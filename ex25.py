#Write a Python program to find whether a given number (accept from the user) is even or odd, 
#print out an appropriate message to the user
n = int(input("Enter a number: "))
if n%2==0:
    print("{} is a even number. ".format(n))
else:
    print("{} is a odd number. ".format(n))