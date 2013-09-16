#Joshua Bloch
#2/05/13
#Colored Windows
import Tkinter
import random
randomNumber=random.randint(1,4)
window=Tkinter.Tk()
colors=['red','blue', 'green', 'yellow']
window.configure(bg=colors[randomNumber])
window.mainloop()

