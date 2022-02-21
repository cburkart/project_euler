# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#
# Find the sum of all the primes below two million.

def is_prime(n):
    """
    Primality test using 6k+-1 optimization.
    Based on the fact that all primes greater than 3 are of the form 6k ± 1 (k is an integer > 0)
    """
    if n <= 3:
        return n > 1
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i ** 2 <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

primes = []
i = 0

while i < 2000000:
    # Check if i is prime
    if is_prime(i):
        primes.append(i)
    # Increment i
    i += 1

print(f'The {i}th prime is {len(primes)} elements long')

print(sum(primes))