#Joshua Bloch
#1/24/12
#Name and Age

user_name=raw_input('Enter your first and last name: ')
user_age=int(raw_input('Enter your age: '))
var1, var2=user_name.split()
print ('Your first name has '), len(var1), ('letters')
print ('Your last name has '), len(var2), ('letters')
print ('Next year you will be '), user_age+1
