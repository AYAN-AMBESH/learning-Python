#Write a Python program to calculate the sum of three given numbers, if the values are equal then return thrice of their sum.
num1 = input("ENTER NUMBER: ")
num3 = input("ENTER NUMBER: ")
num2 = input("ENTER NUMBER: ")
def Sum_of_num(num1,num2,num3):
    sum = num1 + num2 + num3
    if num1 == num2 == num3:
        sum *= 3
    return sum

print(Sum_of_num(1,2,3))
print(Sum_of_num(3,3,3))