# Ethan Busbee

from Clan import *
from Person import *
from Resource import *
from World import *

w = World()

a1 = Area(name = "Marf")
a2 = Area(name = "Bark")

r1 = Resource(kind = "water", maximum = 1000, amount = 925, delta = 5)
r2 = Resource(kind = "food", maximum = 1000, amount = 75, delta = -5)

a1.addResources(r1, r2)

w.addArea(a1)

print "Beginning iteration test."

for i in range(20):
  print "Step " + str(i) + ":"
  for area in w.getAreas():
    print "  Area: " + area.getName()
    for res in area.getResources():
      print "    Resource: " + res.getKind() + "(" + str(res.getAmount()) + ")"
  w.advance()
