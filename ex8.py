#Give a single command that computes the sum from Exercise R-1.7, 
#relying on Python’s comprehension syntax and the built-in sum function
def Square(n):
    return sum(v**2 for v in range(n))   
print(Square(5))