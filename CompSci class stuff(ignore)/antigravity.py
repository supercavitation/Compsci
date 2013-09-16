#Joshua Bloch
#2/05/13
#Age Calculator
import datetime
year=int(raw_input('Enter the year you were born (yyyy): '))
month=int(raw_input('Enter the month you were born (mm): '))
day=int(raw_input('Enter the day you were born (dd): '))

yearsOld=(datetime.date.today().year-year)
monthsOld=(datetime.date.today().month-month)
daysOld=(datetime.date.today().day-day)
if monthsOld<0 and daysOld<0:
    age=yearsOld-1
else:
    age=yearsOld
print age
if monthsOld==0 and daysOld==0:
    print 'Happy Birthday'
