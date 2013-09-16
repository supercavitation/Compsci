#Joshua Bloch
#1/24/13
#Tip Calculator

meal_price=float(raw_input ('Price of meal (in dollars): '))
tip_size=float(raw_input ('% to tip: '))
print ('You should tip '), round(meal_price*tip_size/100, 2), ('dollars')
