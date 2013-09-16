#Joshua Bloch
#2/04/13
#Unit Converter
while True:
    print '''1) Kilometers to Miles
2) Kilograms to Pounds
3) Liters to Gallons
4) Celsius to Farenheit
5) Quit'''

    whichUnit=int(raw_input('Choose a number: '))
    if whichUnit==1:
        kilometers=float(raw_input('Enter the number of Kilometers: '))
        miles=kilometers*0.621
        print kilometers ,'kilometers is', miles, 'miles.'
    elif whichUnit==2:
        kilograms=float(raw_input('Enter the number of Kilograms: '))
        pounds=kilograms*0.454
        print kilograms,'kilograms is', pounds, 'pounds.'
    elif whichUnit==3:
        liters=float(raw_input('Enter the number of Liters: '))
        gallons=liters*0.264
        print liters, 'liters is', gallons, 'gallons.'
    elif whichUnit==4:
        celsius=float(raw_input('Enter the number of degrees in Celsius: '))
        farenheit=celsius*1.8+32
        print celsius, 'degrees celsius is', farenheit, 'degrees farenheit.'
    elif whichUnit==5:
        break
    else:
        print ("That's not an option.")


