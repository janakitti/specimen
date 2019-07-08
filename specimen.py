import random
import time

w, h = 6, 6;

field = [[0 for x in range(w)] for y in range(h)]
print(field)

class Specimen:
    def __init__(self, colour, speed, pos, energy):
        self.colour = colour
        self.speed = speed
        self.pos = pos
        self.energy = energy


    def getAttributes(self):
        return "Colour: {} \nSpeed: {} \nPos: {} \nEnergy: {}".format(self.colour, self.speed, self.pos, self.energy)

    def getPos(self):
        return self.pos

    def specimenMove(self):
        if (self.energy > 0):
            if (self.pos.get('x') == 0):
                moveX = random.randint(0,1)
            elif (self.pos.get('x') == 5):
                moveX = random.randint(-1,0)
            else:
                moveX = random.randint(-1,1)

            if (self.pos.get('y') == 0):
                moveY = random.randint(0,1)
            elif (self.pos.get('y') == 5):
                moveY = random.randint(-1,0)
            else:
                moveY = random.randint(-1,1)

            self.pos['x'] += moveX
            self.pos['y'] += moveY

            self.energy -= abs(moveX + moveY)

pop = []

spec1 = Specimen("red", 2, {'x':0, 'y': 0}, 100)

pop.append(spec1)

print(pop[0].getAttributes() + "\n")

while True:
    pop[0].specimenMove()
    print(pop[0].getAttributes() + "\n")
    field[pop[0].getPos().get('x')][pop[0].getPos().get('y')] = pop[0]
    print(field)

    time.sleep(0.5)
    field = [[0 for x in range(w)] for y in range(h)]




