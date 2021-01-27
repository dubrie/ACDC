import re

class Acdc():

  def __init__(self, power_input=None):
    self.value = None
    self.unit = None
    self.__pattern = "^\d*\.?\d+"
    self.__valid_units = ['lbs/twh','lbs/gwh','lbs/mwh','lbs/kwh','lbs/wh','lbsco2e','gco2e','w','kwh','mwh','gwh','twh','watts','kilowatts','gigawatts','megawatts','terrawatts']

    if power_input is not None:
      self.parse(power_input)
    
  def parse(self, power_input):
    match = re.search(self.__pattern, power_input)
    if match: 
      units = re.split(self.__pattern, power_input)
      if units[1] and units[1].strip().lower() in self.__valid_units:
        self.value = match.group()
        self.unit = units[1].strip().lower()
        return self
    else:
      self.value = None
      self.unit = None
      return None

          
  def toString(self, delimiter=" "):
    return self.value + delimiter + self.unit
