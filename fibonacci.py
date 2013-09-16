#Joshua Bloch
#3/11/13
#fibonacci
def fibonacci(term):
    if term==1 or term==2:
        return 1
    else:
        return fibonacci(term-2)+fibonacci(term-1)
