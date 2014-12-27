# Ethan Busbee
# Project Clanager -- Person Class
# File creation: 2014-12-23

import traceback

from Clan import *
from Resource import *


class Person(object):

  def __init__(self, name):
    super(Person, self).__init__()
    try:
      self._name = str(name)  # Name of Person
      self._clan = None       # Clan Person belongs to
      self._needs = []        # Person's needs (begins empty)
      self._energy = 100      # Person's energy (low = hungry)
      self._water = 100       # Person's hydration (low = thirsty)
      self._health = 100      # Person's health (low = dying)
      self._alive = True      # Whether Person is alive or not
    except:
      print "\n\n" + str(traceback.format_exc())
      print "\n\nDATA VALIDATION ERROR: Person not created!"

  def __del__(self):
    self._name = "DELETED"
    self._clan = None
    self._needs = []
    self._energy = 0
    self._water = 0
    self._health = 0
    self._alive = False

  ### Accessor Methods

  def getName(self):
    return self._name

  def getClan(self):
    return self._clan

  def getNeeds(self):
    return self._needs.items()

  def getEnergy(self):
    return self._energy

  def getHealth(self):
    return self._health

  def isAlive(self):
    return self._alive

  ### Mutator Methods

  # Needs are not going to be done like this forever, this is VERY placeholder
  def changeClan(self, clan):
    if type(clan) is Clan:
      self._clan = clan

  def addNeed(self, need):
    self._needs.append(need)

  def removeNeed(self, need):
    self._needs.remove(need)

  def addEnergy(self, energy):
    try:
      energy = int(energy)
      if energy < 0: raise Exception("Energy added cannot be less than 0.")
    except: print "\n\n" + str(traceback.format_exc()); return False
    self._energy = self._energy + energy

  def takeEnergy(self, energy):
    try:
      energy = int(energy)
      if energy < 0: raise Exception("Energy taken cannot be less than 0.")
      if self._energy - energy < 0: raise Exception("Not enough energy!")
    except: print "\n\n" + str(traceback.format_exc()); return False
    
    self._energy = self._energy - energy
    return True

  def addHealth(self, health):
    try:
      health = int(health)
      if health < 0: raise Exception("Health added cannot be less than 0.")
    except: print "\n\n" + str(traceback.format_exc()); return False

    self._health = self._health + health
    return True

  def removeHealth(self, health):
    try:
      health = int(health)
      if health < 0: raise Exception("Health taken cannot be less than 0.")
    except: print "\n\n" + str(traceback.format_exc()); return False

    self._health = self._health - health
    
    if self._health < 0:  # If the Person died from this damage
      self.health = 0
      self._alive = False

    return True

  ### Simulation Methods

  def iterateSimulation(self):
    self._energy = self._energy - 1
    self._water = self._water - 1