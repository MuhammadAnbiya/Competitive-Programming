def convert_temperature():
    try:
        celsius = float(input("Masukkan suhu dalam Celcius: "))

        fahrenheit = celsius * 9 / 5 + 32
        kelvin = celsius + 273.15

        print(f"Fahrenheit: {fahrenheit:.2f}")
        print(f"Kelvin: {kelvin:.2f}")

    except ValueError:
        print("Error: Invalid input.")

if __name__ == "__main__":
    convert_temperature()