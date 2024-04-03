def parse_constants_file(file_path):
    constants = {}
    with open(file_path, 'r') as file:
        # Skip the header line
        next(file)
        for line in file:
            # Split the line into name, value, and dimension
            name, value, dimension = line.strip().split(',')
            # Store in the dictionary
            constants[name] = {'value': float(value), 'dimensions': dimension}
    return constants

def print_constant_info(constants):
    print("Select a constant to print:")
    for i, constant in enumerate(constants.keys()):
        print(f"{i + 1}. {constant}")
    selection = int(input("Enter the number corresponding to the constant: "))
    constants_list = list(constants.keys())
    selected_constant = constants_list[selection - 1]
    print(f"\n{selected_constant}:")
    print(f"Value: {constants[selected_constant]['value']}")
    print(f"Dimensions: {constants[selected_constant]['dimensions']}")

# Example usage:
file_path = 'constants.txt'
constants = parse_constants_file(file_path)
print_constant_info(constants)
