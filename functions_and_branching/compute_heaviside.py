import math

def compute_smoothed_heaviside(position, epsilon=0.01):
    return 0.5 * (1 + (2 / math.pi) * math.atan(position / epsilon))

def test_smoothed_heaviside():
    # Test case 1: epsilon = 0.01
    epsilon = 0.01
    positions = [-10, -25, 0, -5, 10]
    expected_values = [compute_smoothed_heaviside(pos, epsilon) for pos in positions]
    print("Test case 1: epsilon =", epsilon)
    for i, pos in enumerate(positions):
        print(f"Smoothed Heaviside({pos}) = {expected_values[i]}")

    # Test case 2: epsilon = 0.1
    epsilon = 0.1
    expected_values = [compute_smoothed_heaviside(pos, epsilon) for pos in positions]
    print("\nTest case 2: epsilon =", epsilon)
    for i, pos in enumerate(positions):
        print(f"Smoothed Heaviside({pos}) = {expected_values[i]}")

    # Test case 3: epsilon = 1
    epsilon = 1
    expected_values = [compute_smoothed_heaviside(pos, epsilon) for pos in positions]
    print("\nTest case 3: epsilon =", epsilon)
    for i, pos in enumerate(positions):
        print(f"Smoothed Heaviside({pos}) = {expected_values[i]}")

test_smoothed_heaviside()

def heaviside_step(x):
    if x < 0:
        return 0
    elif x == 0:
        return 0.5
    else:
        return 1

# Test the function
def test_heaviside():
    x_values = [-10, -10-15, 0, 10-15, 10]
    for x in x_values:
        print(f"Heaviside({x}) = {heaviside_step(x)}")

test_heaviside()
test_smoothed_heaviside()