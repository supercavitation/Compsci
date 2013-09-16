#usr/bin/python
# import the main method to test the running time or sort functions on different list sizes.

import time
import random

def merge(left,right):
    result=[]
    i,j=0,0
    while i<len(left) and j<len(right):
        if left[i]<=right[j]:
            result.append(left[i])
            i=i+1
        else:
            result.append(right[j])
            j=j+1
    result=result+left[i:]
    result=result+right[j:]
    return result

def example_sort(values):
    if len(values)<=1:
        return values
    middle=int( len(values)/2)
    left=example_sort(values[:middle])
    right=example_sort(values[middle:])
    return merge(left,right)

def random_list_gen(length):
	#normally I would import this method from another script I have
	rlist = [int(length*random.random()) for i in xrange(length)]
	return rlist
	
def main(sort_function):
	max_size = 8 #Decrease this for bad sorts that take too long
	length = [10**x for x in range (1, max_size)]
	rlist = [random_list_gen(x) for x in length]
	for i in range(0, len(rlist)):
		t1 = time.clock()
		sorted_list = sort_function(rlist[i])
		t2 = time.clock()
		sort_time = t2 - t1
		worked = (sorted_list == sorted(rlist[i]))
		if (worked == True):
			print 'It worked!'
		else:
			print 'Woops... Your sort didn\'t work'
		print 'Your sort took', sort_time, 'seconds for sample size', len(rlist[i]), '.'
		
if (__name__ == '__main__'):
	#Executes the main method on the built in python sort as an example.
	main(example_sort)
	
# You can use this to test some random sorting function by putting it in the same directory
# cding to that directory in the terminal, running python in the terminal, then:
# import sort_tester
# from some_sort_function_script import some_sort_function
# sort_tester.main(some_sort_function)
# 
# Stuff comes out.
