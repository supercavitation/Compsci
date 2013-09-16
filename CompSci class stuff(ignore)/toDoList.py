#Joshua Bloch
#4/9/13
#to do list

choreList=[]
while True:
    chores=raw_input('')
    if chores[0:3]=='add':
        choreList.append(chores[4:])
    elif chores[0:6]=='delete':
        choreList.remove(chores[7:])
    elif chores[0:5]=='print':
        for chore in choreList:
            print chore
    elif chores[0:4]=='quit':
        break
        
