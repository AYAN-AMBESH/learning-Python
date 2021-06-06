#Write a Python program to get a new string from a given string where "Is" 
# has been added to the front. If the given string already begins with "Is" 
# then return the string unchanged.
def string(name):
    if len(name) >= 2 and name[:2]=="Is":
        return name
    return 'IS' + name

name="Array"
print(string(name))
name="Isempty"
print(string(name))