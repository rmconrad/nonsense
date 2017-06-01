import math

def find_next_square(sq):
    #Return the next square if sq is a square, -1 otherwise
    if (math.sqrt(sq) % math.sqrt(sq)) != 1:
        return -1
    else n = ((math.sqrt(sq) + 1) ** 2):
        return n

find_next_square(121)
