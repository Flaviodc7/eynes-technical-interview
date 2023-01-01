# Given an array, return min, max and average of the numbers

def min_max_average(array_numbers):
    return tuple([min(array_numbers), max(array_numbers), sum(array_numbers) / len(array_numbers)])


print(min_max_average([4, 8, 1, 25]))
# Returns (1, 25, 9.5)
