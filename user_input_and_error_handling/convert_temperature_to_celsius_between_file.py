def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def main():
    # Read Fahrenheit temperatures from the input file
    with open("temperature_data.txt", "r") as f:
        lines = f.readlines()

    fahrenheit_temperatures = []
    for line in lines:
        # Skip empty lines or lines that don't contain temperature data
        if line.strip() and "Fahrenheit degrees:" in line:
            # Extract the Fahrenheit temperature from the line
            temperature = float(line.split(":")[1].strip())
            fahrenheit_temperatures.append(temperature)

    # Convert Fahrenheit temperatures to Celsius
    celsius_temperatures = [fahrenheit_to_celsius(temp) for temp in fahrenheit_temperatures]

    # Write Fahrenheit and Celsius temperatures to the output file
    with open("output_temperature_data.txt", "w") as f:
        f.write("Fahrenheit degrees\tCelsius degrees\n")
        for fahrenheit, celsius in zip(fahrenheit_temperatures, celsius_temperatures):
            f.write(f"{fahrenheit}\t\t\t{celsius}\n")

if __name__ == "__main__":
    main()
