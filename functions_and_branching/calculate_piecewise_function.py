def compute_piecewise_constant_function(position, constant_breaks):
    for i, (start, constant) in enumerate(constant_breaks):
        if i == len(constant_breaks) - 1 or position < constant_breaks[i + 1][0]:
            return constant
    return None  # This should never be reached if the breaks are properly defined

# Test the function
def test_piecewise_function():
    # Test case 1: Position before the first segment
    constant_breaks = [(0, 1), (2, -1), (4, 0)]
    position = -1
    expected_result = 1
    result = compute_piecewise_constant_function(position, constant_breaks)
    assert result == expected_result, f"Test case 1 failed. Expected: {expected_result}, Got: {result}"

    # Test case 2: Position within each segment
    constant_breaks = [(0, 1), (2, -1), (4, 0)]
    positions = [1, 3, 4]
    expected_results = [1, -1, 0]
    for pos, expected_result in zip(positions, expected_results):
        result = compute_piecewise_constant_function(pos, constant_breaks)
        assert result == expected_result, f"Test case 2 failed for position {pos}. Expected: {expected_result}, Got: {result}"

    # Test case 3: Position after the last segment
    constant_breaks = [(0, 1), (2, -1), (4, 0)]
    position = 5
    expected_result = 0
    result = compute_piecewise_constant_function(position, constant_breaks)
    assert result == expected_result, f"Test case 3 failed. Expected: {expected_result}, Got: {result}"

    print("All test cases passed!")

# Run the test
test_piecewise_function()