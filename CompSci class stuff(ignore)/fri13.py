#Joshua Bloch
#2/14/13 <3
#Friday the 13th
import calendar
import datetime
x=0
y=datetime.date.today().year
months=datetime.date.today().month
for month in range(months, 13):
    day=calendar.weekday(y,month,13)
    if day==4:
        print month, '/13/', y
        x=x+1
while x<10:
    for month in range (1,13):
        weekday=calendar.weekday(y+1,month,13)
        if weekday==4:
            print month, '/13/', y+1
            x=x+1
        if x==10:
            break
    y=y+1
