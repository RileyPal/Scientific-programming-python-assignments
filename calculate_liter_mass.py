def convert_mass(Kilograms):
    # Conversion factors densities in kg/m^3 divided by 1000 to get in liters per kg
    kg_per_liter_iron = 7870.0/1000
    kg_per_liter_air = 1.2/1000
    kg_per_liter_gasoline = 755.0/1000
    kg_per_liter_platinum = 21450.0/1000

    # Perform conversions
    litersi = Kilograms / kg_per_liter_iron
    litersa = Kilograms / kg_per_liter_air
    litersg = Kilograms / kg_per_liter_gasoline
    litersp = Kilograms / kg_per_liter_platinum

    return litersi, litersa, litersg, litersp

def main():
    # Get input from user
    Kilograms = float(input("Enter mass in Kilograms: "))

    # Perform conversion
    iron, air, gasoline, platinum = convert_mass(Kilograms)

    # Print results
    print(f"{Kilograms} Kilograms is equal to:")
    print(f"{iron:.2f} liters of iron")
    print(f"{air:.2f} liters of air")
    print(f"{gasoline:.2f} liters of gasoline")
    print(f"{platinum:.2f} liters of platinum")

if __name__ == "__main__":
    main()
