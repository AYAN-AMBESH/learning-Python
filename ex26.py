#Write a Python program to count the number 4 in a given list
l=[1,2,3,4,5,6,4,4,4,4,5,2,4,9]
c=0
for l in l:
    if l==4:
        c+=1

print("{} is the number of times 4 comes in the list".format(c))