import sympy as sp


def construct_polynomial_from_roots(x, roots):
    symbolic_poly = 1
    for root in roots:
        symbolic_poly *= (sp.symbols(x) - root)
    expanded_poly = sp.expand(symbolic_poly)
    return expanded_poly, symbolic_poly


def get_roots_from_user():
    roots = []
    print("Enter the constants of the roots one at a time (enter 'q' to stop after entering last constant):")
    while True:
        user_input = input("Enter roots: ")
        if user_input.lower() == 'q':
            break
        # Split the user input by spaces or commas and convert to float
        roots.extend(map(float, user_input.replace(',', ' ').split()))
    return roots


# Test case
def test_construct_polynomial_from_roots():
    roots = [1, 2, 3]  # Roots of the polynomial
    x = 'x'  # Variable in the polynomial
    polynomial, symbolic_poly = construct_polynomial_from_roots(x, roots)

    # Constructed polynomial: P(x) = (x - 1)(x - 2)(x - 3)
    expected_polynomial = 'x**3 - 6*x**2 + 11*x - 6'
    assert str(polynomial) == expected_polynomial, f"Expected: {expected_polynomial}, Got: {polynomial}"

    # Constructed symbolic polynomial: P(x) = (x - 1)*(x - 2)*(x - 3)
    expected_symbolic_poly = "(x - 1)*(x - 2)*(x - 3)"
    assert sorted(str(symbolic_poly)) == sorted(
        expected_symbolic_poly), f"Expected: {expected_symbolic_poly}, Got: {symbolic_poly}"

    print("Test passed!")


def main():
    roots = get_roots_from_user()
    x = 'x'  # Variable in the polynomial
    polynomial, symbolic_poly = construct_polynomial_from_roots(x, roots)
    reduced_form = str(polynomial)

    print("Constructed polynomial (symbolic):", reduced_form)


# Call the main function
if __name__ == "__main__":
    test_construct_polynomial_from_roots()
    main()
