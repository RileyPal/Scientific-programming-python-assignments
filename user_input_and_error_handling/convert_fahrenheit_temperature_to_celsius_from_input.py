def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius

def main():
    # Ask the user for input
    fahrenheit = float(input("Enter the temperature in Fahrenheit: "))

    # Convert Fahrenheit to Celsius
    celsius = fahrenheit_to_celsius(fahrenheit)

    # Print the result
    print(f"{fahrenheit} degrees Fahrenheit is equal to {celsius:.2f} degrees Celsius.")

if __name__ == "__main__":
    main()
