print("=== Temperature Converter ===")

temp = float(input("Enter Temperature: "))
scale = input("Enter Scale (C/F/K): ").upper()

if scale == "C":
    fahrenheit = (temp * 9/5) + 32
    kelvin = temp + 273.15
    print("Fahrenheit:", round(fahrenheit, 2))
    print("Kelvin:", round(kelvin, 2))

elif scale == "F":
    celsius = (temp - 32) * 5/9
    kelvin = celsius + 273.15
    print("Celsius:", round(celsius, 2))
    print("Kelvin:", round(kelvin, 2))

elif scale == "K":
    celsius = temp - 273.15
    fahrenheit = (celsius * 9/5) + 32
    print("Celsius:", round(celsius, 2))
    print("Fahrenheit:", round(fahrenheit, 2))

else:
    print("Invalid Scale! Please enter C, F, or K.")