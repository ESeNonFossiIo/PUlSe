"""
  This is a Class to keep track of error and output of a project.
"""

class Log(object):

  def __init__(self, lenght=100, verbose = False, filename = None):
    self.lenght   = lenght
    self.log_vars = dict()
    self.verbose = verbose
    self.filename = filename
    
  def new_entry(self, name, var, output=False):
    self.log_vars[name] = var
    if output:
      print name + "  = " + var

  def add_action(self, action, vars):
    print "TODO"