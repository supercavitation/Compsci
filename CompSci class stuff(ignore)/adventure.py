#Joshua Bloch
#2/05/13
#Adventure Game
import time
print 'You wake up slowly, standing up, and wearing some fancy form of armor.'
time.sleep(2)
print 'In your hands is a strange rifle. You don\'t recognize it, but somehow, you know exactly how to use it.'
time.sleep(3)
print 'You find yourself standing in a long hallway, with a door behind you.'
time.sleep(2)
print 'You try the door, but you find that it is locked. You proceed down the hallway, and encounter a floating robot.'
time.sleep(4)
print 'It asks, "What is your name?"'
time.sleep(2)
name=raw_input('You respond, "')
print 'It pauses, then responds, "Hello,', name, ', you will be given ten bullets, and your armor will be powered up.'
time.sleep(4)
print '"Are you ready? Anything you find is yours to keep."'
time.sleep(2)
print '"Yes," you hear yourself responding, though you don\'t even know what you just agreed to do.'
time.sleep(3)
print 'You step through the door, and hear an electronic powering up noise.'
time.sleep(2)
print 'Your gun displays a bullet counter, which says that you have 10 bullets left.'
time.sleep(2)
print 'Somehow you know that any bullets you find, you will be able to load into your gun.'
time.sleep(2)
print 'A robot with a single glowing eye pops out from behind an overturned car and aims a rifle at you.'
time.sleep(3)
print 'Do you shoot it first, or attempt to reason with it?'
time.sleep(2)
firstChoice=raw_input('SHOOT or REASON?: ')
if firstChoice=='REASON':
    print 'You call out to the robot, "Hi, can you tell me what I\'m doing here?"'
    time.sleep(2)
    print 'The robot does not respond, so you call out again.'
    time.sleep(2)
    print '"Hi, can you at least tell me where I am? I wish I knew, but I don\'t."'
    time.sleep(2)
    print "The robot fires a burst of bullets over your head, then aims at you again."
    time.sleep(2)
    print 'What do you do? You can shoot it, or you can try to reason with it again.'
    time.sleep(2)
    secondChoice=raw_input('SHOOT or REASON?: ')
    if secondChoice=='REASON':
        print 'The robot fires two shots into your chest, crushing your armor, before you even have a chance to speak.'
        time.sleep(3)
        print 'You fall to the floor, clutching at your chest, feeling the blood flowing out through your fingers.'
        time.sleep(3)
        print 'You look up, one last time, and gasp, "What?" even as the robot fires its last bullet into your head.'
        time.sleep(3)
        print 'The robot confiscates your bullets and walks away, leaving your body on the floor to rot.'
        time.sleep(3)
        print 'You wake up a little while later in a phone booth.'
        time.sleep(2)
        print 'You step out of the phone booth and fly away.'
        time.sleep(2)
        print 'Congratulations, you won!!'
    else:
        print 'You raise your gun and fire two shots into the robot\'s head, shattering it.'
        time.sleep(2)
        print 'Unfortunately, the robot simply grows a new head, and fires a shot at you, which you dodge.'
        time.sleep(3)
        print 'You charge it, knocking it over and slamming it into the ground, then break off both of its legs.'
        time.sleep(3)
        print 'It regrows both legs, but you stab the sharp edge of the legs into each leg, pinning them to the ground.'
        time.sleep(4)
        print 'You pick up its bullets, and look around just in time for the robot to begin beeping.'
        time.sleep(2)
        print 'You dive away, but you aren\'t fast enough to dodge the shrapnel, which pierces your brain, killing you instantly.'
        time.sleep(4)
        print 'You wake up a little while later in a phone booth.'
        time.sleep(2)
        print 'You step out of the phone booth and fly away.'
        time.sleep(2)
        print 'Congratulations, you won!!'
else:
    print 'Like all humans, your first reaction when faced with apathy is to immediately become violent.'
    time.sleep(2)
    print 'You raise your rifle and fire, but your weapon fires too fast.'
    time.sleep(2)
    print 'All ten rounds are fired before you even have a chance to pull your finger off the trigger.'
    time.sleep(2)
    print 'Fortunately, your rounds have the desired impact, tearing open circuits inside the robot\'s chest, turning it into a pile of scrap metal.'
    time.sleep(4)
    print 'You walk over, and find that the robot had 20 bullets, which you load into your gun. Maybe this time, you\'ll be able to save some ammo.'
    time.sleep(4)
    print 'As you stand back up, however, another robot pops out and hits you hard in the back, slamming you to the floor.'
    time.sleep(4)
    print 'You look up, and the robot pauses as it aims at your head.'
    time.sleep(2)
    print 'You can see the reflection of its round counter on its chest, which reads 140. It has killed several people before.'
    time.sleep(4)
    print 'Do you shoot at it, or do you let it kill you?'
    time.sleep(2)
    secondChoice=raw_input ('SHOOT or DIE?: ')
    if secondChoice=='DIE':
        print 'You go limp, hoping that the robot will kill you quickly, and spare you the pain of a bullet wound.'
        time.sleep(3)
        print 'The robot looks down at you, then pauses and turns away. Apparently, the thrill of the chase is preferable to the easy victory.'
        time.sleep(4)
        print 'You lie on the ground for a little while, hoping that the robot will leave and you can go.'
        time.sleep(3)
        print 'The robot eventually turns, and you hop up and begin running.'
        time.sleep(2)
        print 'The robot whirls in an instant and fires two bullets through each leg, and you fall to the ground.'
        time.sleep(3)
        print 'This time, the robot does not take pity on you. It raises its rifle, and aims at your head.'
        time.sleep(3)
        print 'The robot fires a burst, and your head explodes.'
        time.sleep(2)
        print 'You wake up a little while later in a phone booth.'
        time.sleep(2)
        print 'You step out of the phone booth and fly away.'
        time.sleep(2)
        print 'Congratulations, you won!!'
    else:
        print 'You raise your rifle and fire a burst, these ten rounds damaging the robot but not destroying it.'
        time.sleep(3)
        print 'The robot returns fire, but you are able to roll out of the way before its rounds hit you.'
        time.sleep(3)
        print 'You fire your remaining ammo into the damaged points on the robot\'s skin, and it explodes messily, shrapnel bouncing off your armor.'
        time.sleep(4)
        print 'You get up slowly and pick up the robot\'s bullets, then scan the landscape.'
        time.sleep(2)
        print 'You don\'t see anything but hills. It slowly dawns on you that you\'ll be doing this for the rest of your life, how ever long that is.'
        time.sleep(4)
        print 'You lose.'
