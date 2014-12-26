# Ethan Busbee
# Project Clanager -- Clan Class
# File creation: 2014-12-23

import traceback

from Person import *


class Clan(object):

  def __init__(self, name):
    try:
      self._name = str(name)
      self._members = set()
    except:
      print "\n\n" + str(traceback.format_exc())
      print "\n\nDATA VALIDATION ERROR: Clan not created!"
      return

  def __del__(self):
    self._name = "DELETED"
    self._members = set()

  ### Accessor Methods

  def getName(self):
    return self._name

  def getMembers(self):
    return self._members

  ### Mutator Methods

  def addMembers(self, *people):
    for newguy in people:
      if type(newguy) is Person:
        self._members.add(newguy)
      else: return False
    return True

  def removeMembers(self, *people):
    for oldguy in people:
      if type(oldguy) is Person:
        self._members.remove(oldguy)
      else: return False
    return True
