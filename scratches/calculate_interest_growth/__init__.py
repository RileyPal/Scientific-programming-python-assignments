# Importing necessary libraries
import datetime


# Function to compute the growth amount
def compute_growth_amount(initial_amount, interest_rate, years):
    # Convert interest rate from percent to decimal
    interest_rate_decimal = interest_rate / 100

    # Compute the growth amount formula
    growth_amount = initial_amount * (1 + interest_rate_decimal) ** years

    return growth_amount

def get_interest_rate():
    return 4.87  # 12/2/2024


# Main function
def main():
    # Get current date
    current_date = datetime.date.today()

    # Get the interest rate
    interest_rate = get_interest_rate()

    # Initial amount
    initial_amount = 1000

    # Number of years
    years = 3

    # Compute growth amount
    growth_amount = compute_growth_amount(initial_amount, interest_rate, years)

    # Print results
    print("Initial amount: $", initial_amount)
    print("Interest rate: ", interest_rate, "% per year")
    print("Growth amount after", years, "years: $", round(growth_amount, 2))


# Entry point of the program
if __name__ == "__main__":
    main()