# Ethan Busbee
# Project Clanager -- World Class (lol)
# File creation: 2014-12-24

import traceback

from Area import *


class World(object):

  def __init__(self):
    self._areas = set()

  def __del__(self):
    self._areas = set()

  def getAreas(self):
    return self._areas

  def addArea(self, area):
    if type(area) is Area:
      self._areas.add(area)
      return True
    return False

  def removeArea(self, area):
    if type(area) is Area:
      self._areas.remove(area)
      return True
    return False