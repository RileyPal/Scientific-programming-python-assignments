# convert_units.py

"""
Contains functions to convert between different units
"""

__author__ = 'Riley'


def convert_units(value, from_units, to_units):
    """
    Converts a value from one set of units to another
    :param value: float :: value to be converted
    :param from_units: str :: units of the value to be converted from
    :param to_units: str :: units to be converted to
    :return: float :: value in the requested units
    """
    # Define conversion factors
    conversion_factors = {
        'bohr3/atom': 0.14818471147216278,  # cubic bohr to cubic angstroms
        'rydberg/atom': 13.605693122994,     # rydberg to electron volts
        'rydberg/bohr3': 14710.507848260711,  # rydberg per cubic bohr to gigapascals
        'Angstrom3/atom': 1.0,
        'eV/atom': 1.0,
        'GPa': 1.0
    }

    # Perform conversion
    converted_value = value * conversion_factors[from_units] / conversion_factors[to_units]

    return converted_value


# Test cases
if __name__ == "__main__":
    # Test conversion factors
    print("1 cubic bohr per atom equals", convert_units(1, 'bohr3/atom', 'bohr3/atom'), "cubic angstroms per atom")
    print("1 rydberg per atom equals", convert_units(1, 'rydberg/atom', 'rydberg/atom'), "electron volts per atom")
    print("1 rydberg per cubic bohr equals", convert_units(1, 'rydberg/bohr3', 'rydberg/bohr3'), "gigapascals")
