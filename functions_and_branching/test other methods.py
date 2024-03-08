import math
import cmath
import io
import unittest
from contextlib import redirect_stdout

def quadratic_solver(a, b, c):
    """
    Solves the quadratic equation ax^2 + bx + c = 0.
    Returns the roots (real or complex).
    """
    print(f"Equation: {a}x^2 + {b}x + {c}")

    # Calculate the discriminant
    discriminant = b**2 - 4 * a * c

    if discriminant > 0:
        # Real roots
        root1 = (-b + math.sqrt(discriminant)) / (2 * a)
        root2 = (-b - math.sqrt(discriminant)) / (2 * a)
        print("Has two real roots:")
        print(f"Root 1: {root1}")
        print(f"Root 2: {root2}")
    elif discriminant == 0:
        # Double root
        root1 = -b / (2 * a)
        print("Has a double root:")
        print(f"Root: {root1}")
    else:
        # Complex roots
        root1 = (-b + cmath.sqrt(discriminant)) / (2 * a)
        root2 = (-b - cmath.sqrt(discriminant)) / (2 * a)
        print("Has two complex roots:")
        print(f"Root 1: {root1}")
        print(f"Root 2: {root2}")

class TestQuadraticSolver(unittest.TestCase):
    def test_single_root(self):
        a, b, c = 1, 2, 1
        expected_output = "Has a double root:\nRoot: -1.0\n"
        with io.StringIO() as buf, redirect_stdout(buf):
            quadratic_solver(a, b, c)
            output = buf.getvalue()
        self.assertEqual(output, expected_output)

    def test_float_roots(self):
        a, b, c = 1, -2, -3
        expected_output = "Has two real roots:\nRoot 1: 3.0\nRoot 2: -1.0\n"
        with io.StringIO() as buf, redirect_stdout(buf):
            quadratic_solver(a, b, c)
            output = buf.getvalue()
        self.assertEqual(output, expected_output)



if __name__ == "__main__":
    unittest.main()