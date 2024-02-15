# Function to compute equations
def compute_equations(variables_a, variables_b):
    var_a1, var_a2 = variables_a
    var_b1, var_b2 = variables_b

    alabel_2_first = var_a1**2
    blabel_2_first = var_b1**2

    alabel_2_second = var_a2**2
    blabel_2_second = var_b2**2

    binomial_sum_squared_terms_first = alabel_2_first + 2*var_a1*var_b1 + blabel_2_first
    binomial_difference_squared_terms_first = alabel_2_first - 2*var_a1*var_b1 + blabel_2_first
    binomial_sum_squared_first = (var_a1 + var_b1)**2
    binomial_difference_squared_first = (var_a1 - var_b1)**2

    binomial_sum_squared_terms_second = alabel_2_second + 2*var_a2*var_b2 + blabel_2_second
    binomial_difference_squared_terms_second = alabel_2_second - 2*var_a2*var_b2 + blabel_2_second
    binomial_sum_squared_second = (var_a2 + var_b2)**2
    binomial_difference_squared_second = (var_a2 - var_b2)**2

    print(f'First First equation:  {binomial_sum_squared_first:.1f} = {binomial_sum_squared_terms_first:.1f}')
    print(f'First Second equation: {binomial_difference_squared_first:.1f} = {binomial_difference_squared_terms_first:.1f}')

    print(f'Second First equation:  {binomial_sum_squared_second:.1f} = {binomial_sum_squared_terms_second:.1f}')
    print(f'Second Second equation: {binomial_difference_squared_second:.1f} = {binomial_difference_squared_terms_second:.1f}')

# Main function
def main():
    # Input variables as tuples
    variables_a = (3, 3)
    variables_b = (5, 3)

    # Compute equations
    compute_equations(variables_a, variables_b)

# Entry point of the program
if __name__ == "__main__":
    main()