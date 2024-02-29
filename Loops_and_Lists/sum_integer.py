def sum_of_integers(maximum_integer):
    total = 0
    for i in range(1, maximum_integer + 1):
        total += i
    return total


def arithmetic_series_sum(maximum_integer):
    return maximum_integer * (maximum_integer + 1) / 2


def main():
    maximum_integer = 100  # Define the maximum_integer
    sum_using_loop = sum_of_integers(maximum_integer)
    sum_using_formula = arithmetic_series_sum(maximum_integer)

    print("Using a for loop:")
    print(f"Sum of integers from 1 to {maximum_integer}: {sum_using_loop}")

    print("\nUsing the arithmetic series formula:")
    print(f"Sum of integers from 1 to {maximum_integer}: {sum_using_formula}")

    print("\nComparison:")
    print(f"Difference between the two methods: {abs(sum_using_loop - sum_using_formula)}")


if __name__ == "__main__":
    main()