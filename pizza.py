#Joshua Bloch
#5/20/13
#Pizza

import math

class Pizza:
    def __init__(self,diameter):
        self.diameter=float(diameter)
        self.toppings=[]
        self.cost=0.00
    def __str__(self):
        return 'A '+str(self.diameter)+' inch pizza with:'
    def addTopping(self, topping):
        if topping not in self.toppings:
            self.toppings.append(topping)
            self.cost+=0.75
    def printToppings(self):
        return self.toppings
    def cost(self):
        self.cost+=math.pi*(0.5*self.diameter)**2*0.15
        self.cost=round(self.cost,2)
        return self.cost

pizza=Pizza(10)
pizza.addTopping("Mushrooms")
pizza.addTopping('Tomatoes')
pizza.addTopping('Garlic')
toppings=pizza.printToppings()
print pizza
for line in toppings:
    print line
print Pizza.cost(pizza)

        
