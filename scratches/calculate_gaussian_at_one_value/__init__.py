import math


# Define the Gaussian function
def gaussian_function(x, mu, sigma):
    # Calculate the exponent term
    exponent = -0.5 * ((x - mu) / sigma) ** 2

    # Calculate the coefficient term
    coefficient = 1 / (sigma * math.sqrt(2 * math.pi))

    # Calculate the value of the Gaussian function
    result = coefficient * math.exp(exponent)

    return result


# Define mean (mu) and standard deviation (sigma)
mu = 0
sigma = 1

# Evaluate the Gaussian function at a specific point
x = 1
result = gaussian_function(x, mu, sigma)
print("using math as library for Gaussian function PDF at x =", x, ":", result)
#or
from scipy.stats import norm

# Define mean (mu) and standard deviation (sigma) for the Gaussian distribution
mu = 0
sigma = 2

# Create a Gaussian distribution object
gaussian_dist = norm(loc=mu, scale=sigma)

# Evaluate the Gaussian function at a specific point
x = 1
pdf_value = gaussian_dist.pdf(x)  # Probability Density Function (PDF) value at x
print("using scipy as library for Gaussian function PDF at x =", x, ":", pdf_value)

print("Mean =", mu)
print("standard deviation =", sigma)
print("input value =", x)
print("Scipy's result is the same as wolfram alpha's")

