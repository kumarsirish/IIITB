
class Temperature:
    def from_fahrenheit(self,f):
        """Convert Fahrenheit to Celsius."""
        return (f - 32) * 5.0 / 9.0

temperature = Temperature()
fahrenheit_temp =212
celsius_temp = temperature.from_fahrenheit(fahrenheit_temp)
print(f"{fahrenheit_temp}°F is equal to {celsius_temp:.1f}°C")