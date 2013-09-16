#Josh Cohen
#3/14/13
#Money grabbing game

from Tkinter import *
import random

score_value = 0

x0 = 15 #The inital coords of the "person"
y0 = 15
x1 = 30
y1 = 30

single_x = random.randint(40,500) #Cords for the money
single_y = random.randint(40,500)
two_x = random.randint(40,500)
two_y = random.randint(40,500)
five_x = random.randint(40,500)
five_y = random.randint(40,500)
ten_x = random.randint(40,500)
ten_y = random.randint(40,500)
twenty_x = random.randint(40,500)
twenty_y = random.randint(40,500)
fifty_x = random.randint(40,500)
fifty_y = random.randint(40,500)
hundred_x = random.randint(40,500)
hundred_y = random.randint(40,500)
penny_x = random.randint(40,500)
penny_y = random.randint(40,500)
nickle_x = random.randint(40,500)
nickle_y = random.randint(40,500)
dime_x = random.randint(40,500)
dime_y = random.randint(40,500)
quarter_x = random.randint(40,500)
quarter_y = random.randint(40,500)
half_dollar_x = random.randint(40,500)
half_dollar_y = random.randint(40,500)

def personA(event): #Animates the "person" by deletezing the one before and creating a new one with new coords



global x0, y0, x1, y1, person



if (event.keysym == "Up"):



canvas.delete(person)



y0 -= 3



y1 -= 3



person = canvas.create_oval(x0, y0, x1, y1, fill='yellow')



elif(event.keysym == "Down"):



canvas.delete(person)



y0 += 3



y1 += 3



person = canvas.create_oval(x0, y0, x1, y1, fill='yellow')



elif(event.keysym == "Left"):



canvas.delete(person)



x0 -= 3



x1 -= 3



person = canvas.create_oval(x0, y0, x1, y1, fill='yellow')



elif(event.keysym == "Right"):



canvas.delete(person)



x0 += 3



x1 += 3



person = canvas.create_oval(x0, y0, x1, y1, fill='yellow')

def coins_or_bills(): #Spawns coins or bills with random values



money_value = random.randint(1,12) #Generates a random number for spawning different money values 



if money_value == 1:



one_dollar_bill = canvas.create_text(single_x, single_y, text='$1.00')



elif money_value == 2:



two_dollar_bill = canvas.create_text(two_x, two_y, text='$2.00')



elif money_value == 3:



five_dollar_bill = canvas.create_text(five_x, five_y, text='$5.00')



elif money_value == 4:



ten_dollar_bill = canvas.create_text(ten_x, ten_y, text='$10.00')



elif money_value == 5:



twenty_dollar_bill = canvas.create_text(twenty_x, twenty_y, text='$20.00')



elif money_value == 6:



fifty_dollar_bill = canvas.create_text(fifty_x, fifty_y, text='$50.00')



elif money_value == 7:



one_hundred_dollar_bill = canvas.create_text(hundred_x, hundred_y, text='$100.00')



elif money_value == 8:



penny = canvas.create_text(penny_x, penny_y, text='1 c')



elif money_value == 9:



nickle = canvas.create_text(nickle_x, nickle_y, text='5 c')



elif money_value == 10:



dime = canvas.create_text(dime_x, dime_y, text='10 c')



elif money_value == 11:



quarter = canvas.create_text(quarter_x, quarter_y, text='25 c')



else:



half_dollar = canvas.create_text(half_dollar_x, half_dollar_y, text='50 c')
def score_collection():



if x0 >= single_x and x0 <= single_x + 1 and y0 >= single_y and y0 <= single_y + 10 and x1 <= single_x and x1 >= single_x-10 and y1 <= single_y and y1 >= single_y-10:



score += 1



canvas.delete(one_dollar_bill)

window = Tk()
window.title('Money Game')
canvas = Canvas(window, width = 600, height = 600) #Creates the widnow
canvas.pack()
person = canvas.create_oval(x0, y0, x1, y1, fill='yellow') #creates the "person" with specicific initial coords
window.bind("<Key>", personA) #Calling the functions that responds to the arrow keys being pushed for animated the "person"
coins_or_bills()
score = Tk()
score.title('Score')
score_canvas = Canvas(score, width = 200, height = 100)
score_canvas.pack()
visual_score = score.create_text(100, 50, text=score)
score_collection()
score.mainloop()
window.mainloop()
