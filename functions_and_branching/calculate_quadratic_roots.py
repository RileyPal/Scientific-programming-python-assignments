import cmath

def calculate_quadratic_roots(a, b, c):
    """
    Solves the quadratic equation ax^2 + bx + c = 0.
    Returns the roots (real or complex).
    """
    # Calculate the discriminant
    discriminant = b**2 - 4 * a * c

    if discriminant > 0:
        # Real roots
        root1 = (-b + cmath.sqrt(discriminant)) / (2 * a)
        root2 = (-b - cmath.sqrt(discriminant)) / (2 * a)
        return root1, root2
    elif discriminant == 0:
        # Double root
        root = -b / (2 * a)
        return root,
    else:
        # Complex roots
        root1 = (-b + cmath.sqrt(discriminant)) / (2 * a)
        root2 = (-b - cmath.sqrt(discriminant)) / (2 * a)
        return root1, root2



# Test function for single root
def test_single_root():
    inputs = (1, 2, 1)
    expected_output = (-1.0,)
    roots = calculate_quadratic_roots(*inputs)
    assert roots == expected_output, f"Failed for inputs {inputs}. Expected {expected_output}, but got {roots}"

# Test function for real roots
def test_roots_float():
    inputs = (1, -2, -3)
    expected_output = (3.0, -1.0)
    roots = calculate_quadratic_roots(*inputs)
    assert roots == expected_output, f"Failed for inputs {inputs}. Expected {expected_output}, but got {roots}"

# Test function for complex roots
def test_roots_complex():
    inputs = (2, 2, -1)
    expected_output = (1j, -1j)
    roots = calculate_quadratic_roots(*inputs)
    assert roots == expected_output, f"Failed for inputs {inputs}. Expected {expected_output}, but got {roots}"

# Run all the tests
test_single_root()
test_roots_float()
test_roots_complex()

print("All tests passed successfully!")
