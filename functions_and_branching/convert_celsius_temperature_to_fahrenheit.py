def celsius_to_fahrenheit(temperature):
    return (temperature * 9 / 5) + 32


def fahrenheit_to_celsius(temperature):
    return (temperature - 32) * 5 / 9


while True:
    user_input = input(
        "Celsius or Fahrenheit (type 'exit' to quit): ").lower()  # Convert input to lowercase for easier comparison

    if user_input == "exit":
        break

    if user_input in ("f", "fahrenheit"):
        temperature = float(input("Enter temperature in Fahrenheit: "))
        print("Temperature in Celsius:", fahrenheit_to_celsius(temperature))
    elif user_input in ("c", "celsius"):
        temperature = float(input("Enter temperature in Celsius: "))
        print("Temperature in Fahrenheit:", celsius_to_fahrenheit(temperature))
    else:
        print("Invalid input. Please enter 'Celsius' or 'Fahrenheit'.")
