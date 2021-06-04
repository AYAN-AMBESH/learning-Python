#Write a Python program to concatenate all elements in a list into a string and return it
def concatenate(ulist):
    return "".join(ulist)
        

input_list = input("ENTER YOUR LIST : ").split()
print(concatenate(input_list))