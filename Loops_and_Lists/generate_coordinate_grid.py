# Define the range parameters
x = 1
y = 2
n = 20

# Calculate the interval
interval = (y - x) / n

# Generate the list of coordinates
coordinates = [(x + i * interval, x + (i + 1) * interval) for i in range(n)]

# Print the list of coordinates
print(coordinates)