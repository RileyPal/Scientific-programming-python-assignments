# I enter 12 Km for my running of the code
def convert_distance(kilometers):
    # Conversion factors
    inches_per_km = 39370.1
    feet_per_km = 3280.84
    yards_per_km = 1093.61
    miles_per_km = 0.621371

    # Perform conversions
    inches = kilometers * inches_per_km
    feet = kilometers * feet_per_km
    yards = kilometers * yards_per_km
    miles = kilometers * miles_per_km

    return inches, feet, yards, miles

def main():
    # Get input from user
    kilometers = float(input("Enter distance in kilometers: "))

    # Perform conversion
    inches, feet, yards, miles = convert_distance(kilometers)

    # Print results
    print(f"{kilometers} kilometers is equal to:")
    print(f"{inches:.2f} inches")
    print(f"{feet:.2f} feet")
    print(f"{yards:.2f} yards")
    print(f"{miles:.2f} miles")

if __name__ == "__main__":
    main()
