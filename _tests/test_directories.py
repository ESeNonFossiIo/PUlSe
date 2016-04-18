import sys
sys.path.append("./_lib/")
sys.path.append("./../_lib/")
import os
from PUlSe_directories import *
from PUlSe_bash_utilities import *
from PUlSe_log import *

def test_make_next_dir():
  base_dir = "_tmp/"

  print os.path.dirname(os.path.realpath(__file__))
  work_dir = os.path.dirname(os.path.realpath(__file__))
  os.chdir(work_dir)
  
  #log = LogFile()
  mkdir(base_dir)
  rmdir(base_dir)
  
  assert not os.path.isdir("./"+base_dir)

  print os.listdir("./")
  next_dir = make_next_dir( progress_dir="run", 
                            separation_char="_", 
                            base_directory=base_dir,
                            lenght=4)
  print os.listdir("./")
  print next_dir
  print os.path.join(next_dir)
  print os.path.exists(base_dir+next_dir)
  assert os.path.exists("./"+os.path.join(next_dir))


  try:
    print " Removing " + base_dir +"run_0000"
    os.removedirs(base_dir+"run_0000")
  except:
    pass
