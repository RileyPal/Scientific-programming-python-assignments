# Parameters
x_values = [1, 2]
num_intervals = 20
h = (x_values[1] - x_values[0]) / num_intervals

# Using a for loop
print("Using a for loop:")
x_for_loop = []
for i in range(num_intervals + 1):
    x = x_values[0] + i * h
    x_for_loop.append(round(x, 2))
print("x =", x_for_loop)

# Using list comprehension
print("Using list comprehension:")
x_list_comp = [round(x_values[0] + i * h, 2) for i in range(num_intervals + 1)]
print("x =", x_list_comp)
