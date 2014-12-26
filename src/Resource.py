# Ethan Busbee
# Project Clanager -- Resource Class
# File creation: 2014-12-23

import traceback


class Resource(object):

  def __init__(self, kind, amount):
    super(Resource, self).__init__()
    try:
      self._kind = str(kind)
      self._amount = int(amount)
    except:
      print "\n\n" + str(traceback.format_exc())
      print "\n\nDATA VALIDATION ERROR: Resource not created!"
      return

  def __del__(self):
    self._kind = "DELETED"
    self._amount = 0

  def _calculateHarvestAmount(self):
    return min(self._amount, 5)

  ### Accessor Methods

  def getKind(self):
    return self._kind

  def getAmount(self):
    return self._amount

  ### Mutator Methods

  def harvest(self):
    if self._amount < 1:
      harvestAmount = 0
    else:
      harvestAmount = self._calculateHarvestAmount()

    self._amount = self._amount - harvestAmount
    return (self._kind, amount)
