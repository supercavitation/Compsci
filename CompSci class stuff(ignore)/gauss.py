#Joshua Bloch
#2/12/13
#gauss
total=0
number=int(raw_input('Add up all of the numbers between 1 and: '))
difference=int(raw_input('What should the difference between each number be? '))
for i in range (1,number+1):
    if (difference*(i-1))+1<=101:
        total=total+((difference*(i-1))+1)
print total
