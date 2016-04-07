"""
  This is a Class to deal with strings.
"""

def get_name_inside(  line, 
                      begin_container="(", 
                      end_container=")"):
  """ Get the value inside a container.
  
    Capture the text contained between two containers.

    Args:
      line (str): Text string
      begin_container (str): This delimiter is the one before the value to capture.
      end_container (str): This delimiter is the one after the value to capture.
      
    Returns:
      string: value contained between `begin_container` and `end_container`.
  """
  assert begin_container!="", " ERROR: `begin_container` is empty."
  assert end_container!="", " ERROR: `end_container` is empty."
  size = len(begin_container)
  start = line.find(begin_container)+size
  end = line.find(end_container, start)
  if end > -1 and start > -1:
    return line[start:end] 
  else :
    return ""

def fill_dictionary_with_config_parser( dictionary, 
                                        confparser, 
                                        section):
  """ Use a ConfigParser to fill a dictionary.
  
    Capture the text contained between two containers.

    Args:
      dictionary (dict): Dictionary to fill.
      confparser (ConfigParser): ConfigParser Object where to take data for 
        filling `dictionary`.
      section (str): Name of the section where to take data to fill the
        dictionary.
  """
  for entry in confparser.options(section):
    dictionary[entry] = confparser.get(section, entry)