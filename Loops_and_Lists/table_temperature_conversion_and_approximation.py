def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9

def fahrenheit_to_Approximate(fahrenheit):
    return (fahrenheit - 30) / 2

def main():
    print("Fahrenheit\tCelsius\tApproximate Celsius")
    print("-------------------------")

    fahrenheit = 0
    while fahrenheit <= 100:
        celsius = fahrenheit_to_celsius(fahrenheit)
        approximate_celsius = fahrenheit_to_Approximate(fahrenheit)  # Corrected the call here
        print(f"{fahrenheit}\t\t{celsius:.2f}\t\t{approximate_celsius:.2f}")  # Corrected variable name
        fahrenheit += 10

if __name__ == "__main__":
    main()