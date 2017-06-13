good_list = []
bad_list = []

def sum_two_smallest_numbers(numbers):
    for num in numbers:
        if num > 0:
            good_list.append(num)
            sorted(good_list)
        else:
            bad_list.append(num)

    return sorted(good_list)[0] + sorted(good_list)[1]

print(sum_two_smallest_numbers([10, 110, 12, -33]))
