def find_next_square(sq):
    #Return the next square if sq is a square, -1 otherwise
    root = sq ** 0.5
    if root.is_integer():
        return (root + 1) ** 2
    else:
        return -1


# Dewey's Version:
#
# #! /path/to/python
#
# import math
# import sys
#
# dude = float(sys.argv[1])
#
# def perfect_sq():
#         n = dude
#         if n == int(math.sqrt(n)) ** 2:
#                 print “square”
#         else:
#                 print “not a square”
# perfect_sq()
