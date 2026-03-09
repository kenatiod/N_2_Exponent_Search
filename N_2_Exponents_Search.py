# N_2_Exponents_Search.py
"""
This program goes through an envelope of prime divisor exponents to find
products of n(n+1) that are prime-complete (i.e. are divisible by all prime
numbers from their greatest prime divisor down to 2 without gaps).

The initial envelope from 2 to 37 are {12, 11, 9, 7, 6, 4, 4, 3, 3, 3, 2, 2}.
This can be changed or extended as needed. Because we are using an array of
prime number exponents that have no gaps, the numbers generated will
always be prime-complete. The test to see if that product of the prime
divisors (raised to the envelope powers) is also a product of consecutive 
integers, the integer square root is taken, and then multiplied by itself 
plus one, and checked to see if that recovers the original product.

by Ken Clements, Feb. 20, 2026
"""

from math import isqrt

primes = [0] + [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 
        47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103]
max_pidx = 27

exponent_envelope = [0] + [12, 11, 9, 7, 6, 4, 4, 3, 3, 3, 2, 2]
len_e = len(exponent_envelope)
prime_exponents = [0] * len_e

print(f"Searching through exponent envelope: ", end="", flush=True)
max_N = 1
for i in range(1, len_e-1):
    max_N *= primes[i] ** exponent_envelope[i]
    print(f"{primes[i]}^{exponent_envelope[i]} x ", end="", flush=True)
print(f"{primes[len_e-1]}^{exponent_envelope[len_e-1]} \n")
max_N *= primes[len_e-1] ** exponent_envelope[len_e-1]
print(f"That gives maximum product = {max_N:,}\n")

def increment_exponents():
    carry, omega = 1, 1
    while carry > 0:
        carry = 0
        prime_exponents[omega] += 1
        if prime_exponents[omega] > exponent_envelope[omega]:
            prime_exponents[omega] = 1
            carry = 1
            omega += 1
            if omega >= len(prime_exponents): return False
    return True

def check_exponents():
    N, omega = 1, 1
    while omega < len(prime_exponents) and prime_exponents[omega] > 0:
        N *= primes[omega] ** prime_exponents[omega]
        omega += 1
    n = isqrt(N)
    if N == n * (n + 1):
        return n
    else:
        return 0   

exponents_tested = 0
found_n_values = 0
while increment_exponents():
    exponents_tested += 1
    result = check_exponents()
    if result > 0:
        print(f"n = {result}")
        found_n_values += 1

print(f"\nOut of {exponents_tested:,} exponents tested, {found_n_values} values of n were found where n(n+1) is prime-complete.")
print(f"\nEnd of Program")

