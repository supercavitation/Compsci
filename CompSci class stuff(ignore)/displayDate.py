#Joshua Bloch
#4/8/13
#display date

import datetime
today=datetime.date.today()
months= ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
weekdays= ['Monday','Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
print 'Today is', weekdays[today.weekday()]+',', months[today.month-1], today.day, today.year
