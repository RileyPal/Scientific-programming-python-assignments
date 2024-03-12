import math

def trapezoidal_rule(f, a, b, n):
    h = (b - a) / n
    integral = (f(a) + f(b)) / 2
    for i in range(1, n):
        integral += f(a + i * h)
    integral *= h
    return integral

def cos_integral(a, b, tolerance=1e-4):
    n = 1
    integral_approx = 0  # Initialize integral_approx
    error = float('inf')
    while error > tolerance:
        integral_approx = trapezoidal_rule(math.cos, a, b, n)
        integral_exact = math.sin(b) - math.sin(a)
        error = abs(integral_exact - integral_approx)
        n *= 2  # Double the number of trapezoids
    return integral_approx, n

def sin_integral(a, b, tolerance=1e-4):
    n = 1
    integral_approx = 0  # Initialize integral_approx
    error = float('inf')
    while error > tolerance:
        integral_approx = trapezoidal_rule(math.sin, a, b, n)
        integral_exact = -math.cos(b) + math.cos(a)
        error = abs(integral_exact - integral_approx)
        n *= 2  # Double the number of trapezoids
    return integral_approx, n

def main():
    # Define integration bounds
    a = 0
    b = math.pi
    b_half = math.pi / 2

    # Compute integrals and required trapezoids
    cos_integral_pi, n_cos = cos_integral(a, b)
    sin_integral_pi, n_sin = sin_integral(a, b)
    sin_integral_pi_half, n_sin_half = sin_integral(a, b_half)

    # Print results
    print("Integral of cos(x) from 0 to pi:", cos_integral_pi)
    print("Error in integral of cos(x) from 0 to pi:", abs(math.sin(b) - math.sin(a)) - cos_integral_pi)
    print("Number of trapezoids used for cos(x) integration:", n_cos)
    print("Integral of sin(x) from 0 to pi:", sin_integral_pi)
    print("Error in integral of sin(x) from 0 to pi:", abs(-math.cos(b) + math.cos(a)) - sin_integral_pi)
    print("Number of trapezoids used for sin(x) integration:", n_sin)
    print("Integral of sin(x) from 0 to pi/2:", sin_integral_pi_half)
    print("Error in integral of sin(x) from 0 to pi/2:", abs(-math.cos(b_half) + math.cos(a)) - sin_integral_pi_half)
    print("Number of trapezoids used for sin(x) integration (0 to pi/2):", n_sin_half)

if __name__ == "__main__":
    main()