import numpy.random as random

def gen_number_with_exception(low, high, exception1, exception2):
    num = random.randint(low, high)
    while num == exception1 or num== exception2:
        num = random.randint(low, high)
    return num

print gen_number_with_exception(0, 20, 15, 10)
