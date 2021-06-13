#Write a Python program to get a string which is n (non-negative integer) copies of a given string.
def String(output , n ):
    output = output *n
    return output

print(String('abc',10))