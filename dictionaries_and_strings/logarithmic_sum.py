def sum_series(x_value, number_of_terms):
    summation = 0
    for index in range(1, number_of_terms + 1):
        summation += (1.0 / index) * (x_value / (1.0 + x_value))**index
    return summation


def calculate_sum_and_error(x_value, number_of_terms):
    summation = 0
    for index in range(1, number_of_terms + 1):
        summation += (1.0 / index) * (x_value / (1.0 + x_value))**index
    sum_value = summation
    next_term = (1.0 / (number_of_terms + 1)) * (x_value / (1.0 + x_value))**(number_of_terms + 1)
    from math import log
    exact_error = log(1 + x_value) - sum_value
    return sum_value, next_term, exact_error


def print_sum_table(x_value, file=None):  # Add file argument
    from math import log
    print('\nx=%g, ln(1+x)=%g' % (x_value, log(1 + x_value)), file=file)  # Change print statement
    for number_of_terms in [1, 2, 10, 100, 500]:
        value, next_term, error = calculate_sum_and_error(x_value, number_of_terms)
        print('n=%-4d %-10g  (next term: %8.2e  '
              'error: %8.2e)' % (number_of_terms, value, next_term, error), file=file)  # Change print statement


def calculate_sum_with_epsilon(x_value, epsilon=1.0E-6):
    x_value = float(x_value)
    index = 1
    term = (1.0 / index) * (x_value / (1 + x_value))**index
    summation = term
    while abs(term) > epsilon:
        index += 1
        term = (1.0 / index) * (x_value / (1 + x_value))**index
        summation += term
    return summation, index


def print_epsilon_table(x_value, file=None):  # Add file argument
    from math import log
    for index in range(4, 14, 2):
        epsilon = 10**(-index)
        approximation, number_of_terms = calculate_sum_with_epsilon(x_value, epsilon=epsilon)
        exact = log(1 + x_value)
        exact_error = exact - approximation
        print('epsilon: %5.0e, exact error: %8.2e, n=%d' %
              (epsilon, exact_error, number_of_terms), file=file)  # Change print statement


if __name__ == '__main__':
    with open('logarithmic_sum.out', 'w') as f:  # Open file in write mode
        print_sum_table(10, file=f)
        print_sum_table(100, file=f)
        print_sum_table(1000, file=f)

        print('\n\n', file=f)
        print_epsilon_table(10, file=f)