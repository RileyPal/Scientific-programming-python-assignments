import math

def sinusoidal_sum(time, number_of_functions, period):
    result = 0
    for n in range(1, number_of_functions + 1):
        result += math.sin(2 * math.pi * n * time / period) / n
    return result

def piecewise_function(time, period):
    if time < period / 2:
        return 1
    else:
        return -1

def compute_error(time, number_of_functions, period):
    true_value = piecewise_function(time, period)
    approx_value = sinusoidal_sum(time, number_of_functions, period)
    return abs(true_value - approx_value)

def main():
    periods = [0.01, 0.25, 0.49]
    number_of_functions = [1, 3, 5, 10, 30, 100]

    print("Results:")
    print("n        \tt        \tError")
    for n in number_of_functions:
        for period in periods:
            for alpha in [0.01, 0.25, 0.49]:
                time = 2 * math.pi * alpha
                error = compute_error(time, n, period)
                print(f"{n}\t{time}\t{error}")

if __name__ == "__main__":
    main()