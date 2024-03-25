import math


def gaussian(position, mean=0.0, standard_deviation=1.0):
    coefficient = 1 / (standard_deviation * math.sqrt(2 * math.pi))
    exponent = -0.5 * ((position - mean) / standard_deviation) ** 2
    return coefficient * math.exp(exponent)


def main():
    # Prompt user for input
    mean = float(input("Enter the mean of the Gaussian distribution: "))
    standard_deviation = float(input("Enter the standard deviation of the Gaussian distribution: "))

    # Calculate the range of x values
    start_x = mean - 5 * standard_deviation
    end_x = mean + 5 * standard_deviation

    # Calculate the spacing between x values
    num_points = 11  # Including both endpoints
    step = (end_x - start_x) / (num_points - 1)

    # Print the header of the table
    print("x\tf(x)")

    # Calculate and print the x and f(x) values
    for i in range(num_points):
        x = start_x + i * step
        fx = gaussian(x, mean, standard_deviation)
        print(f"{x:.2f}\t{fx:.6f}")

if __name__ == "__main__":
    main()