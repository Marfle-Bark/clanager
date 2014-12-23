# Ethan Busbee
# Project Clanager -- Resource Class
# File creation: 2014-12-23

class Resource(object):

  def __init__(self, kind = "NONE", amount = 0):
    self._checkInputs(kind = kind, amount = amount)

  def __del__(self):
    self._kind = "DELETED"
    self._amount = 0

  def _checkInputs(self, kind, amount):
    print "kind = " + kind
    print "amount = " + amount