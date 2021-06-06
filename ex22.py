# Write a Python program to calculate the sum of three given numbers
# if the values are equal then return three times of their sum.
def Sum(x,y,z):
    if x==y==z:
        return 3 *(x+y+z)
    return x+y+z

x=int(input())
y=int(input())
z=int(input())
print(Sum(x,y,z))