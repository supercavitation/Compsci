from robotworld import World, Robot
#
wld=World("row1")
#
sparky=Robot(wld,beepers=0)
#
sparky.move()
sparky.pickBeeper()
sparky.move()
sparky.pickBeeper()
sparky.move()
sparky.pickBeeper()
sparky.move()
sparky.pickBeeper()
sparky.move()
sparky.pickBeeper()
sparky.move()
sparky.pickBeeper()
sparky.move()
while sparky.anyBeepersInBeeperBag():
    sparky.putBeeper()
sparky.move()


wld.mainloop()
