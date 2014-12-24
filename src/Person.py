# Ethan Busbee
# Project Clanager -- Person Class
# File creation: 2014-12-23

import traceback
from Clan import Clan
from Resource import Resource

class Person(object):

  def __init__(self, name):
    try:
      self._name = str(name)  # Name of Person
      self._clan = None       # Clan Person belongs to
      self._needs = {}        # Person's needs (begins empty)
      self._energy = 100      # Person's energy (low = hungry)
      self._health = 100      # Person's health (low = dying)
      self._alive = True      # Whether Person is alive or not
    except:
      print "\n\n" + str(traceback.format_exc())
      print "\n\nDATA VALIDATION ERROR: Person not created!"

  def __del__(self):
    self._name = "DELETED"
    self._clan = None
    self._needs = {}
    self._energy = 0
    self._health = 0
    self._alive = False

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

  def getAlive(self):
    return self._alive