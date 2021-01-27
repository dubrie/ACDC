import re

class Acdc():

  def __init__(self, power_input=None):
    self.__clear()
    self.__pattern = "^\d*\.?\d+"
    self.__ONE_HOUR = 1
    self.__units = [
        'lbs/twh','lbs/gwh','lbs/mwh','lbs/kwh','lbs/wh',
        'lbsco2e','gco2e',
        'wh','kwh','mwh','gwh','twh',
        'w','kw','mw','gw','tw',
        'watts','kilowatts','gigawatts','megawatts','terrawatts'
    ]

    if power_input is not None:
      self.parse(power_input)
    
  def __clear(self):
      self.value = 0.0
      self.unit = None
      self.basewatts = None

  def parse(self, power_input):
    match = re.search(self.__pattern, power_input)
    if match: 
      units = re.split(self.__pattern, power_input)
      if units[1] and units[1].strip().lower() in self.__units:
        self.value = float(match.group())
        self.unit = units[1].strip().lower()
        self.noramlizeValueToWatts()
        return self
    else:
      self.__clear()
      return None

  def noramlizeValueToWatts(self):
    if self.unit == 'w' or self.unit == 'watts':
        self.basewatts = self.value
    elif self.unit == 'kw' or self.unit == 'kilowatts':
        self.basewatts = (self.value * 1000)
    elif self.unit == 'mw' or self.unit == 'megwatts':
        self.basewatts = (self.value * 1000 * 1000)
    elif self.unit == 'gw' or self.unit == 'gigawatts':
        self.basewatts = (self.value * 1000 * 1000 * 1000)
    elif self.unit == 'tw' or self.unit == 'terrawatts':
        self.basewatts = (self.value * 1000 * 1000 * 1000 * 1000)
    else:
        print("Error: Cannot normalize to watts")        

  def toString(self, delimiter=" "):
    return str(self.value) + delimiter + self.unit

  def convertTo(self,to_unit):
    # convert from basewatts to whatever the request is
    if to_unit == 'w' or self.unit == 'watts':
        self.unit = 'w'
        self.value = self.basewatts
    elif to_unit == 'kw' or self.unit == 'kilowatts':
        self.unit = 'kw'
        self.value = self.basewatts / 1000
    elif to_unit == 'mw' or self.unit == 'megawatts':
        self.unit = 'mw'
        self.value = self.basewatts / 1000 / 1000
    elif to_unit == 'gw' or self.unit == 'gigawatts':
        self.unit = 'gw'
        self.value = self.basewatts / 1000 / 1000 / 1000
    elif to_unit == 'tw' or self.unit == 'terrawatts':
        self.unit = 'tw'
        self.value = self.basewatts / 1000 / 1000 / 1000 / 1000
    elif to_unit == 'wh':
        self.unit = 'wh'
        self.value = (self.basewatts * self.__ONE_HOUR)
    elif to_unit == 'kwh':
        self.unit = 'kwh'
        self.value = (self.basewatts * self.__ONE_HOUR) / 1000
    elif to_unit == 'mwh':
        self.unit = 'mwh'
        self.value = (self.basewatts * self.__ONE_HOUR) / 1000 / 1000
    elif to_unit == 'gwh':
        self.unit = 'gwh'
        self.value = (self.basewatts * self.__ONE_HOUR) / 1000 / 1000 / 1000
    elif to_unit == 'twh':
        self.unit = 'twh'
        self.value = (self.basewatts * self.__ONE_HOUR) / 1000 / 1000 / 1000 / 1000
    else:
        print("ERROR: Can't determine unit: "+to_unit)
