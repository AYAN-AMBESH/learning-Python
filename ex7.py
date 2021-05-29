#Write a short Python function that takes a positive integer n and returns
#the sum of the squares of all the positive integers smaller than n
def Square(n):
    Sum=0
    for i in range(0,n):
        Sum += i**2
    return Sum
print(Square(5))
