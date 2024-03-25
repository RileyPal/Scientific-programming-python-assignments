import math

def calculate_difference_quotient(function, position, interval= 0.01):
    # Calculate the value of the function at position
    fx = function(position)

    # Calculate the value of the function at position + interval
    fx_plus_h = function(position + interval)

    # Calculate the difference quotient
    difference_quotient = (fx_plus_h - fx) / interval

    return difference_quotient


def test_calculate_difference_quotient():
    # Test case 1: f(x) = e^x at x=0
    def my_function(x):
        return math.e ** x
    position = 0
    exact_derivative = 1
    derivative_approximation = calculate_difference_quotient(my_function, position)
    print("Test case 1: Approximation of the derivative of f(x) = e^x at x=0:", derivative_approximation)
    assert abs(derivative_approximation - exact_derivative) <= 0.02, f"Test case 1 failed: {derivative_approximation}"

    # Test case 2: f(x) = e^(-2x^2) at x=0
    def my_function2(x):
        return math.e ** (-2 * x ** 2)
    position2 = 0
    exact_derivative2 = 0
    derivative_approximation2 = calculate_difference_quotient(my_function2, position2)
    print("Test case 2: Approximation of the derivative of f(x) = e^(-2x^2) at x=0:", derivative_approximation2)
    assert abs(derivative_approximation2 - exact_derivative2) <= 0.02, f"Test case 2 failed: {derivative_approximation2}"

    # Test case 3: f(x) = cos(x) at x=2pi
    def my_function3(x):
        return math.cos(x)
    position3 = 2 * math.pi
    exact_derivative3 = 0
    derivative_approximation3 = calculate_difference_quotient(my_function3, position3)
    print("Test case 3: Approximation of the derivative of f(x) = cos(x) at x=2pi:", derivative_approximation3)
    assert abs(derivative_approximation3 - exact_derivative3) <= 0.02, f"Test case 3 failed: {derivative_approximation3}"

    # Test case 4: f(x) = ln(x) at x=1
    def my_function4(x):
        return math.log(x)
    position4 = 1
    exact_derivative4 = float('inf')  # Derivative is not defined at x=1
    derivative_approximation4 = calculate_difference_quotient(my_function4, position4)
    print("Test case 4: Approximation of the derivative of f(x) = ln(x) at x=1:", derivative_approximation4)
    assert abs(derivative_approximation4 / exact_derivative4) <= 1.05 >= 0.95, f"Test case 4 failed: {derivative_approximation4}"

    print("All tests passed!")

# Run the test
test_calculate_difference_quotient()