def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5 / 9
    return celsius


def main():
    # Read the temperature from the file
    with open("temperature_data.txt", "r") as file:
        # Skip the first three lines
        for _ in range(3):
            next(file)

        # Read the fourth line
        line = file.readline().strip()

        # Split the line into words and grab the third word
        words = line.split()
        fahrenheit = float(words[2])

    # Convert Fahrenheit to Celsius
    celsius = fahrenheit_to_celsius(fahrenheit)

    # Print the result
    print(f"{fahrenheit} degrees Fahrenheit is equal to {celsius:.2f} degrees Celsius.")


if __name__ == "__main__":
    main()