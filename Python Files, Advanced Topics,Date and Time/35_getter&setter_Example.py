class Celsius:
    def __init__(self, temperature = 0):
        self._temperature = temperature

    def to_fahrenheit(self):
        return (self._temperature * 1.8) + 32

    @property
    def temperature(self):
        print("Getting Value..")
        return self._temperature
    
    @temperature.setter
    def temperature(self, newTemperature):
        print("Setting value..")
        if newTemperature < -237.15:
            raise ValueError("Temperatue below -237 is not possible")
        self._temperature = newTemperature

    



human = Celsius(37)
print(human._temperature)
print(human.temperature)
print(human.to_fahrenheit())
human._temperature = 45
print(human._temperature)
human.temperature = 67
print(human.temperature)