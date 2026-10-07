# Temperature Conversion Program

unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ")
temp = float(input("Enter the temperature: "))

if unit == "C":
    temp = (9 * temp) / 5 + 32
    print(f"Temperature in Fahrenheit is: {round(temp, 2)} °F")
elif unit == "F":
    temp = round((temp - 32) * 5 / 9)
    print(f"Temperature in Celsius is: {round(temp, 2)} ºC")
else:
    print(f"{unit} is not a valid unit of measurement")