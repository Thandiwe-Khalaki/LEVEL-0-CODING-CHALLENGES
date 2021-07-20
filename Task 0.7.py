def fahrenheit_to_celsius(number):
    return (number - 32) * 5/9

def celsius_to_fahrenheit(number):
    return number * (9/5) + 32


def main():
    print(fahrenheit_to_celsius(0))
    print(celsius_to_fahrenheit(0))

if __name__ == '__main__':
    main()