import re

class Acdc():

  def __init__(self, power_input=None):
    self.__clear()
    self.__pattern = "^\d*\.?\d+"
    self.__ONE_HOUR = 1
    self.__GRAMS_IN_POUND = 453.592
    self.__power_units = [
        'wh','kwh','mwh','gwh','twh',
        'w','kw','mw','gw','tw',
        'watts','kilowatts','gigawatts','megawatts','terrawatts'
    ]
    self.__emissions_units = [
        'lbsco2e','gco2e',
    ]
    if power_input is not None:
      self.parse(power_input)
    
  def __clear(self):
      self.value = 0.0
      self.unit = None
      self.basewatts = None
      self.basegrams = None
      self.power_value = 0.0
      self.power_unit = None
      self.emissions_value = 0.0
      self.emissions_unit = None

  def parse(self, power_input):
    match = re.search(self.__pattern, power_input)
    if match: 
      units = re.split(self.__pattern, power_input)
      if units[1]:
        unit = units[1].strip().lower() 
        if unit in self.__power_units:
            self.value = float(match.group())
            self.unit = unit
            self.noramlizeValueToWatts()
        elif unit in self.__emissions_units:
            self.value = float(match.group())
            self.unit = unit
            self.noramlizeValueToGrams()
        else:
            self.__clear()
            return None
        return self
    else:
      self.__clear()
      return None

  def noramlizeValueToGrams(self):
    if self.unit == 'gco2e':
        self.basegrams = self.value
    elif self.unit == 'lbsco2e':
        self.basegrams = self.value * self.__GRAMS_IN_POUND 
    else:
        print("Error: Cannont normalize to grams:" +self.unit)

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

  def convertPowerTo(self,to_unit):
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


  def convertEmissionsTo(self,to_unit):
    # convert from basegrams to whatever the request is
    if to_unit == 'gco2e':
        self.unit = 'gco2e'
        self.value = self.basegrams
    elif to_unit == 'lbsco2e':
        self.unit = 'lbsco2e'
        self.value = self.basegrams / self.__GRAMS_IN_POUND
    else:
        print("ERROR: Can't determine unit: "+to_unit)

