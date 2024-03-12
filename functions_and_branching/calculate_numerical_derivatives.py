import math

def calculate_difference_quotient(function, position, interval= 0.01):
    # Calculate the value of the function at position
    fx = function(position)

    # Calculate the value of the function at position + interval
    fx_plus_h = function(position + interval)

    # Calculate the difference quotient
    difference_quotient = (fx_plus_h - fx) / interval

    return difference_quotient


def test_difference_quotient():
    # Define a quadratic function: f(x) = ax^2 + bx + c
    def quadratic_function(x):
        a = 2
        b = 3
        c = 1
        return a * x**2 + b * x + c

    # Choose a position for testing
    position = 2

    # Calculate the exact derivative of the quadratic function at the chosen position
    exact_derivative = 11

    # Calculate the approximation of the derivative using the difference quotient
    derivative_approximation = calculate_difference_quotient(quadratic_function, position)

    # Verify if the approximation matches the exact derivative
    if abs(derivative_approximation - exact_derivative) <= 0.02:
        print("Test passed!")
    else:
        print("Test failed!")

# Run the test
test_difference_quotient()


def my_function(x):
    return math.e**x

position = 0
derivative_approximation = calculate_difference_quotient(my_function, position)
print("Approximation of the derivative: of f(x) = e^x at x=0", derivative_approximation)


def my_function2(x):
    return math.e**(-2*x**2)

position2 = 0
derivative_approximation = calculate_difference_quotient(my_function2, position2)
print("Approximation of the derivative: of f(x) = e^-2x^2 at x=0", derivative_approximation)

def my_function3(x):
    return math.cos(x)

position3 = 2*math.pi
derivative_approximation = calculate_difference_quotient(my_function3, position3)
print("Approximation of the derivative: of f(x) = cos(x) at x= 2pi", derivative_approximation)


def my_function4(x):
    return math.log(x)

position4 = 1
derivative_approximation = calculate_difference_quotient(my_function4, position4)
print("Approximation of the derivative: of f(x) = ln(x) at x= 1", derivative_approximation)