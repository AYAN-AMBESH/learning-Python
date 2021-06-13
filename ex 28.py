# Write a Python program to create a histogram from a given list of integers
def histogram(li):
    for l in li:
        a=''
        temp=l
        while(temp>=0):
            a= a +'*'
            temp-=1   
        print(a)
    exit()
print(histogram([2,5,7,1,3]))