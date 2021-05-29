#Write a short Python function, minmax(data), that takes a sequence of
#one or more numbers, and returns the smallest and largest numbers, in the
#form of a tuple of length two. Do not use the built-in functions min or
#max in implementing your solution.
def minmax(data):
    data=(input("ENTER A:"),input("ENTER B:"))
    if data[0] > data[1]:
        print(f"{data[0]} is greater")
    print(f"{data[1]} is greater")
dara=()
minmax(dara)