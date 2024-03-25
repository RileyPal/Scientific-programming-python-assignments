import sys

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def main():
    try:
        # Check if the command line arguments are provided correctly
        if len(sys.argv) != 2:
            raise ValueError("Incorrect number of command line arguments.")

        # Get the Fahrenheit temperature from the command line argument
        fahrenheit = float(sys.argv[1])

        # Convert Fahrenheit to Celsius
        celsius = fahrenheit_to_celsius(fahrenheit)

        # Print the result
        print(f"{fahrenheit} degrees Fahrenheit is equal to {celsius:.2f} degrees Celsius.")
    except ValueError as e:
        print("Error:", e)
        print("Usage: convert_fahrenheit_temperature_to_celsius_from_command_line.py <temperature_in_fahrenheit>")
        sys.exit(1)

if __name__ == "__main__":
    main()

