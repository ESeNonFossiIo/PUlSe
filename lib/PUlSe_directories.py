"""
  This library is a collection of Classes and Functions to deal with folder and
  filenames.
"""

import os

def make_next_dir(  progress_dir="run", 
                    separation_char="_", 
                    base_directory="output/",
                    lenght=4):
  """
    Find the next directory:
    
    :param progress_dir: name of the directory that should have a progress number
    :type progress_dir: string
    :param separation_char: the first value
    :type separation_char: char
    :param base_directory: base name
    :type base_directory: string
    :param lenght: lenght of the progressive folder number
    :type lenght: int
    :returns: name of the new directory
    :rtype: string
  """
  base_directory+="/"
  if not os.path.exists(base_directory):
    os.makedirs(base_directory)

  numbers=[]
  for name in os.listdir(base_directory):
    if (  os.path.isdir(os.path.join(base_directory, name)) and
          name.find(progress_dir)>=0 ) :
      numbers.append( int( str(name).replace(progress_dir + separation_char, '') ) )
  numbers.append(-1)
  maximum = str ( max(numbers) + 1 )
  zeroes =  "0" * ( lenght - len(maximum) )
  new_dir = os.path.normpath(base_directory + progress_dir + separation_char + zeroes + maximum)
  os.makedirs(new_dir)
  
  return new_dir

def get_next( filename = "name", 
              ext = "txt",
              directory = "./",
              separation_char = "_",
              lenght=4):
  """
    Find the next avaible name:

    TODO:
    :param progress_dir: name of the directory that should have a progress number
    :type progress_dir: string
    :param separation_char: the first value
    :type separation_char: char
    :param base_directory: base name
    :type base_directory: string
    :param lenght: lenght of the progressive folder number
    :type lenght: int
    :returns: name of the new directory
    :rtype: string
  """            
  numbers=[]
  for name in os.listdir(directory):
    if ( name.find(filename)>=0 and  name.find(ext)>=0) :
      name = name.replace("."+str(ext),"")
      numbers.append( int( str(name).replace(filename + separation_char, '') ) )
  numbers.append(-1)
  maximum = str ( max(numbers) + 1 )
  zeroes =  "0" * ( lenght - len(maximum) )
  next_filename = filename + separation_char + zeroes + maximum
  return next_filename