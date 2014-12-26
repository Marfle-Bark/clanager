# Ethan Busbee
# Project Clanager -- Resource Class
# File creation: 2014-12-23

import traceback


class Resource(object):

  def __init__(self, kind, maximum, amount, delta):
    super(Resource, self).__init__()
    try:
      self._kind = str(kind)
      self._max = int(maximum)
      if self._max < 0: raise Exception("Max must be >= 0!")
      self._amount = min(int(amount), self._max)
      if self._amount < 0: raise Exception("Amount must be >= 0!")
      self._delta = int(delta)
    except:
      print "\n\n" + str(traceback.format_exc())
      print "\n\nDATA VALIDATION ERROR: Resource not created!"
      return

  def __del__(self):
    self._kind = "DELETED"
    self._max = 0
    self._amount = 0
    self._delta = 0

  def _calculateHarvestAmount(self):
    return min(self._amount, 5)

  ### Accessor Methods

  def getKind(self):
    return self._kind

  def getMax(self):
    return self._max

  def getAmount(self):
    return self._amount

  def getDelta(self):
    return self._delta

  ### Mutator Methods

  def harvest(self):
    if self._amount < 1:
      harvestAmount = 0
    else:
      harvestAmount = self._calculateHarvestAmount()

    self._amount = self._amount - harvestAmount
    return (self._kind, amount)
