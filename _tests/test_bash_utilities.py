import sys
sys.path.append("./lib/")
sys.path.append("./../lib/")
import os
from PUlSe_bash_utilities import *

def test_make_next_dir():
  assert os.path.join( 
    os.path.dirname(os.path.realpath("./")), this_dir(False)) \
    == this_dir(True)