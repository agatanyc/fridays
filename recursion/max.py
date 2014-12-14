def max(numbers, largest_so_far=0):
    if numbers == []:
        return largest_so_far
    next_num = numbers[0]
    if next_num > largest_so_far:
        return max(numbers[1:], next_num)
    else:
        return max(numbers[1:], largest_so_far)

xs = [2, 4, 5, 7, 1, 4]
print(max(xs))
