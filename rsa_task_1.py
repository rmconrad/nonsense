# Task_1:
# write a function called check_print. This will evaluate 2 numbers you enter from the command line
# to determine the numers are prime, since there is no algorithm to find it. lets limit this to the first
# 100 RSA prime numbers (it excludes 2).



primes_100 = [3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,101,103,107,109,113,127,131,137,139,149,151,157,163,167,173,179,181,191,193,197,199,211,223,227,229,233,239,241,251,257,263,269,271,277,281,283,293,307,311,313,317,331,337,347,349,353,359,367,373,379,383,389,397,401,409,419,421,431,433,439,443,449,457,461,463,467,479,487,491,499,503,509,521,523,541,557]


a = int(raw_input('first prime: '))
b = int(raw_input('second prime: '))

def check_print(primes_100,a,b):
    if (a in primes_100 and b in primes_100):
        return dict([('num1', a),('num2', b)])
    else:
        return 'One or both numbers is not a prime.'

print(check_print(primes_100,a,b))
