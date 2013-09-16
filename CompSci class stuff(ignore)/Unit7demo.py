#Joshua Bloch
#5/14/13
#A class to represent a person

class Person:

    def __init__(self,fname,lname,age=0):

        self.first = fname
        self.last = lname
        self.age = age
        self.alive = True

    def __str__(self):
        
        return self.first+' '+self.last

    def birthday(self):
        self.age+=1

    def marry(self,new_last):
        self.last=new_last
        
smeds=Person('Sam','Smedinghoff', 28)
print smeds,smeds.age
silberman=Person('Reuben','Silbermsn', 34)
print silberman, silberman.age
smeds.birthday()
print smeds, smeds.age
smeds.marry('Silberhoff')
silberman.marry('Silberhoff')
print smeds
print silberman
        
