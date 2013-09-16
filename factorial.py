#Joshua Bloch
#3/11/13
#factorial
def factorial(num):
    if num!=1:
        return num*factorial(num-1)
    else:
        return 1
