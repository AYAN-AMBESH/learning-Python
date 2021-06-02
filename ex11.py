#Write a Python program which accepts the user's first and last name and print them in reverse order with a space between them
first_name = input("first name: ")
last_name = input("Enter last name: ")
temp = first_name
first_name = last_name
last_name = temp
print(first_name + " " + last_name)