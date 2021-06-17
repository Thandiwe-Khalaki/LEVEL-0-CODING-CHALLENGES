def fahrenheit_to_celsius(number):
    """Takes a number in Fahrenheit and returns temperature in Celsuis"""
    return (number - 32) * 5/9

def celsius_to_fahrenheit(number):
    """Takes a number in Celsuis and returns temperature in Fahrenheit"""
    return number * (9/5) + 32

print(fahrenheit_to_celsius(0))
print(celsius_to_fahrenheit(0))