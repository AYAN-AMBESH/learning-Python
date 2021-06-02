#Write a Python program which accepts a sequence of comma-separated numbers from user and generate a list and a tuple with those numbers.
num =  input("ENTER VALUES: ")
list = num.split(',')
tuple = tuple(list)
print(list)
print(tuple) 