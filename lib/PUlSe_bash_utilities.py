"""
  This library is a collection of Classes and Functions to replace Bash
  commands in a python script.
"""

import os

def rmdir(directory, error=False, log=None):
  """
    Remove @par directory
    
    :param directory: name of the directory to remove
    :type directory: string
    :param error: return the error assert, otherwise suppress it
    :type error: bool
    :param log: name of the log variable 
    :type base_directory: PUlSe_log.Log
  """

  if log:
    log.add_action(action = "Remove directory", var = directory)

  try:
    os.removedirs(directory)
  except OSError, e:
    if error:
      return e

def mkdir(directory, error=False, log=None):
  """
    Make  :directory:
    
    :param directory: name of the directory to make
    :type directory: string
    :param error: return the error assert, otherwise suppress it
    :type error: bool
    :param log: name of the log variable 
    :type base_directory: PUlSe_log.Log
  """
  if log:
    log.add_action( action = "Make directory", var = directory)

  try:
    os.makedirs(directory)
  except OSError, e:
    if error:
      return e

def this_dir(abs = True):
  """
    Return the path of the current directory
    
    :param abs: return the absolute path of the directory, otherwise only the name
    :type error: bool
    :returns: name of the directory
    :rtype: string
  """
  current_dir = os.getcwd()
  if abs:
    return current_dir
  else:
    return current_dir.split(os.sep)[-1]
  