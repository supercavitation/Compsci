from robotworld import World, Robot
#
wld=World("row1")
#
sparky=Robot(wld,beepers=0)
TARDIS=Robot(wld,x=10,y=1,direction=180)
#
sparky.move()
for i in range(1,2):
    sparky.pickBeeper()
sparky.move()
for i in range(1,3):
    sparky.pickBeeper()
sparky.move()
for i in range(1,4):
    sparky.pickBeeper()
sparky.move()
for i in range(1,5):
    sparky.pickBeeper()
sparky.move()
for i in range(1,6):
    sparky.pickBeeper()
sparky.move()
for i in range(1,7):
    sparky.pickBeeper()
sparky.move()
sparky.move()
for i in range(1,22):
    sparky.putBeeper()
sparky.turnLeft()
sparky.turnLeft()
sparky.move()
TARDIS.move()
for i in range(1,22):
    TARDIS.pickBeeper()

wld.mainloop()
