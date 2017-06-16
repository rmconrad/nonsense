# First RSA prime Number

primes_100 = [3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,101,103,107,109,113,127,131,137,139,149,151,157,163,167,173,179,181,191,193,197,199,211,223,227,229,233,239,241,251,257,263,269,271,277,281,283,293,307,311,313,317,331,337,347,349,353,359,367,373,379,383,389,397,401,409,419,421,431,433,439,443,449,457,461,463,467,479,487,491,499,503,509,521,523,541,557]

 # Task_1:
 # write a function called check_print. This will evaluate 2 numbers you enter from the command line
 # to determine the numers are prime, since there is no algorithm to find it. lets limit this to the first
 # 100 RSA prime numbers (it excludes 2).


 # Task_2:
 # write a function that calculates the modulus and totient of the two prime numbers entered into the script
 # (that pass our test) where:
 # this will be the basis of our public key
 # the modulous is the two prime numbers multiplied together m(p,q)
 # the totient is the  two prime numbers -1 multipled together t(p-1,q-1)

 # Task_3
 # write a function that chooses the public key with a new primary number entry field on the command line.
 # The new outputs should be
 # 1. a check for the validity of the initally chose prime numbers from task_1
 # 2. print the output in the form Modulus(p,q,p*q) and Totient(p-1,q-1,(p-1)(q-1))
 # 3. provide an entry field for any prime number less than the Totient (validate the number for being prime) for the public key (k)


 # Task_4
 # create the secret key (s) using the euclidian extended algorithm
 # We are trying to find the multiplicative inverse of a newly chosen public key (from the entry field)
 # to create our secrete key.
 #
 # The secret key, when multiplied with our public key, should have a remainder of 1 (k*s % t).
 # This is where we apply the euclidian extended algorithm
 #
