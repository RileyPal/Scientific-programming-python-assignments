summation = 0
starting_index = 0
index = starting_index
maximum_index = 100

while index < maximum_index:
    index += 1
    inverse = 1 / index
    summation += inverse
    print(f'sum(k = {starting_index}, {maximum_index}) 1/k = {summation}')
