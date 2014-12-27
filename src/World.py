# Ethan Busbee
# Project Clanager -- World Class (lol)
# File creation: 2014-12-24

import traceback

from Area import *


class World(object):

  def __init__(self):
    super(World, self).__init__()
    self._areas = []

  def __del__(self):
    self._areas = []

  ### Accessor Methods

  def getAreas(self):
    return self._areas

  ### Mutator Methods

  def addArea(self, area):
    if type(area) is Area:
      self._areas.append(area)
      return True
    return False

  def removeArea(self, area):
    if type(area) is Area:
      self._areas.remove(area)
      return True
    return False

  ### Simulation Methods

  def iterateSimulation(self):
    for area in self._areas:
      area.iterateSimulation()
