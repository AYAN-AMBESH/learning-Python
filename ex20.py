# Write a Python program to get the difference between a given number and 17, 
# if the number is greater than 17 return double the absolute difference. 
def number():     
    x = 17
    y = int(input("enter a number: "))
    if y>17:
        return 2*abs(y-x)
    return (x-y)

print(number())