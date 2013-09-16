from robotworld import World, Robot
import random
#
wld=World("maze")
#
sparky=Robot(wld,beepers=0)
while True:
    option=[0]
    if sparky.frontIsClear():
        option.append(1)
    randomNumber=random.randint(0,len(option)-1)
    if randomNumber==0:
        sparky.turnLeft()
    else:
        sparky.move()
    if sparky.frontIsClear() and sparky.leftIsClear() and sparky.rightIsClear() and sparky.backIsClear():
        break
    
wld.mainloop()
