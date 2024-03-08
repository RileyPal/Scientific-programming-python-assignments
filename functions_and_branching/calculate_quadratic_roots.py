import cmath
def solve_quadratic(coefficients):
    a, b, c = coefficients
    discriminant = b**2 - 4*a*c

    if discriminant > 0:
        root1 = (-b + cmath.sqrt(discriminant)) / (2*a)
        root2 = (-b - cmath.sqrt(discriminant)) / (2*a)
        return root1, root2
    elif discriminant == 0:
        root = -b / (2*a)
        return root,
    else:
        real_part = -b / (2*a)
        imaginary_part = cmath.sqrt(abs(discriminant)) / (2*a)
        root1 = real_part + imaginary_part * 1j
        root2 = real_part - imaginary_part * 1j
        return root1, root2

# Test cases
def test_solve_quadratic():
    assert solve_quadratic([1, -3, 2]) == (2.0, 1.0)
    assert solve_quadratic([1, -6, 9]) == (3.0,)
    assert solve_quadratic([1, 2, 3]) == ((-1 + 1.4142135623730951j), (-1 - 1.4142135623730951j))
    print("All test cases passed!")


def get_and_solve_quadratic():
    inputs = []
    print("Enter coefficients a, b, and c:")
    for i in range(3):
        user_input = float(input(f"Enter coefficient {chr(97 + i)}: "))
        inputs.append(user_input)

    roots = solve_quadratic(inputs)
    print("Roots of the quadratic equation:", roots)
# Run the test cases
test_solve_quadratic()
get_and_solve_quadratic()

