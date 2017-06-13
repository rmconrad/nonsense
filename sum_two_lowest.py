data = [100, 11, 12, 33]
good_list = []
bad_list = []

def sum_two_smallest_numbers(numbers):
    for num in numbers:
        if num > 0:
            good_list.append(num)
            sorted(good_list)
        else:
            bad_list.append(num)

print(bad_list)
print(good_list)

print(sum_two_smallest_numbers([data]))




# Works for basic tests, but edits original array
# def sum_two_smallest_numbers(numbers):
#     # orderList = sorted(numbers)
#     # return orderList[0] + orderList[1]
