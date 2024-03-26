def calculate_velocity_and_acceleration(positions, index, time_step=1e-6):
    # Calculate velocity using forward difference
    if index < len(positions) - 1:
        velocity = (positions[index + 1] - positions[index]) / time_step
    else:
        velocity = None  # Cannot calculate velocity at the last position

    # Calculate acceleration using central difference
    if 0 < index < len(positions) - 1:
        acceleration = (positions[index + 1] - 2 * positions[index] + positions[index - 1]) / (time_step ** 2)
    else:
        acceleration = None  # Cannot calculate acceleration at the first or last position

    return velocity, acceleration

def test_kinematics():
    # Define positions and time step
    positions = [1, 2, 3, 4, 5]
    print("positions in 1 second intervals:", positions)
    time_step = 1  # Assume time step of 1 second

    # Define time points to calculate velocity and acceleration
    time_points = [0, 0.5, 1.5, 2.2]

    # Iterate over time points
    for t in time_points:
        # Calculate the index closest to the specified time point
        index = int(t / time_step)

        # Calculate velocity and acceleration at the specified time point
        velocity, acceleration = calculate_velocity_and_acceleration(positions, index, time_step)

        # Print the results
        print(f"At time t = {t} s:")
        print(f"Velocity: {velocity} units/s")
        print(f"Acceleration: {acceleration} units/s^2")
        print()

# Run the test
test_kinematics()