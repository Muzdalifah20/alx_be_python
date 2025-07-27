FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

try:
    user_temperature = int(input("Enter the temperature to convert: "))
except ValueError:
    print("Invalid temperature. Please enter a numeric value.")
    exit()

match temp_kind:
    case "f":
        print(convert_to_celsius(user_temperature))
    case "c":
        print(convert_to_fahrenheit(user_temperature))   
    case _ :
        print("Invalid temperature kind")
    
