# Ethan Busbee
# Project Clanager -- Resource Class
# File creation: 2014-12-23

import traceback

class Resource(object):

  def __init__(self, kind, amount):
    try:
      kind = str(kind)
      amount = int(amount)
    except:
      print "\n\n" + str(traceback.format_exc())
      print "\n\nDATA VALIDATION ERROR"
      return

  def __del__(self):
    self._kind = "DELETED"
    self._amount = 0