#
# Torbert, June 2012
#
from robotworld import World, Robot
#
wld=World("maze")
#
karel=Robot(wld)
#
karel.move()
karel.pickBeeper()
karel.move()
karel.turnLeft()
karel.move()
karel.putBeeper()
karel.move()
karel.turnLeft()
karel.move()
karel.move()
karel.turnLeft()
karel.turnLeft()
karel.turnLeft()
karel.move()

#
wld.mainloop()
#
# END OF FILE
#
