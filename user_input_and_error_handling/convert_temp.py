import sys
import convert_temperature


def main():
    if len(sys.argv) != 3:
        print("Usage: python convert_temperature.py <temperature> <scale>")
        print("Example: python convert_temperature.py 21.3 C")
        return

    temperature_str = sys.argv[1]
    scale = sys.argv[2].upper()

    try:
        temperature = float(temperature_str)
    except ValueError:
        print("Invalid input temperature. Please enter a valid numeric temperature.")
        return

    if scale not in ['C', 'F', 'K']:
        print("Invalid temperature scale. Please enter 'C' for Celsius, 'F' for Fahrenheit, or 'K' for Kelvin.")
        return

    if scale == 'C':
        print("Input temperature:", temperature, "C")
        print("Converted temperatures:")
        print("  Fahrenheit:", convert_temperature.celsius_to_fahrenheit(temperature), "F")
        print("  Kelvin:", convert_temperature.celsius_to_kelvin(temperature), "K")
    elif scale == 'F':
        print("Input temperature:", temperature, "F")
        print("Converted temperatures:")
        print("  Celsius:", convert_temperature.fahrenheit_to_celsius(temperature), "C")
        print("  Kelvin:", convert_temperature.fahrenheit_to_kelvin(temperature), "K")
    elif scale == 'K':
        print("Input temperature:", temperature, "K")
        print("Converted temperatures:")
        print("  Celsius:", convert_temperature.kelvin_to_celsius(temperature), "C")
        print("  Fahrenheit:", convert_temperature.kelvin_to_fahrenheit(temperature), "F")


if __name__ == '__main__':
    main()
