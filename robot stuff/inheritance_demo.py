#Joshua Bloch
#5/21/13
from robotworld import *
class Smartbot(Robot):
    def turnRight(self):
        self.turnLeft()
        self.turnLeft()
        self.turnLeft()

wld=World("maze")

santiago = Smartbot(wld)
santiago.turnLeft()
santiago.move()
santiago.turnRight()
santiago.move()
santiago.turnRight()
santiago.move()
santiago.turnLeft()
santiago.move()
santiago.turnLeft()
santiago.move()
santiago.turnRight()
santiago.move()
santiago.move()
santiago.turnRight()
santiago.move()
santiago.turnLeft()
santiago.move()
santiago.turnLeft()
santiago.move()
santiago.move()
santiago.move()
santiago.move()
santiago.turnRight()
santiago.move()
santiago.move()

wld.mainloop()
