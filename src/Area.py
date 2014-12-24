# Ethan Busbee
# Project Clanager -- Area Class
# File creation: 2014-12-24

import traceback

from Clan import *
from Person import *
from Resrouce import *


class Area(object):

  ID = 1

  def __init__(self, name = None):
    self._people = {}
    self._resources = []
    self._connections = {}
    self._owner = None

    self._ID = ID
    ID = ID + 1

    if name is not None:
      try:
        name = str(name)
        self._name = name
      except:
        print "\n\n" + str(traceback.format_exc())
        print "\n\nDATA VALIDATION ERROR: Area not created!"
        return

  def __del__(self):
    self._people = {}
    self._resources = []
    self._connections = {}
    self._owner = None
    self._ID = 0
    self._name = "DELETED"

  def getPeople(self):
    return self._people

  def getResources(self):
    return self._resources

  def getConnections(self):
    return self._connections

  def getOwner(self):
    return self._owner

  def getID(self):
    return self._ID

  def getName(self):
    return self._name