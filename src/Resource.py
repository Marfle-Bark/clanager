# Ethan Busbee
# Project Clanager -- Resource Class
# File creation: 2014-12-23

import traceback


class Resource(object):

  def __init__(self, kind, maximum, amount, delta):
    super(Resource, self).__init__()
    try:
      self._validateInit(maximum, amount)
      self._kind = str(kind)
      self._max = int(maximum)
      self._amount = min(int(amount), self._max)
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

  ### Validation Methods

  def _validateInit(self, maximum, amount):
    if maximum < 0: raise Exception("Max must be >= 0!")
    if amount < 0: raise Exception("Amount must be >= 0!")

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

  def executeDelta(self):
    if self._delta is not 0:
      self._amount = min(self._max, self._amount + self._delta)
      self._amount = max(self._amount, 0)

  def changeDelta(self, delta):
    try:
      delta = int(delta)
      self._delta = delta
    except:
      print "\n\n" + str(traceback.format_exc())