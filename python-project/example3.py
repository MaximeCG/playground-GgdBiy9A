# Primality test all the numbers from 2 to 9.
for n in range(2, 10):
    # Generator that gives all the divisors of n:
    divisors = (x for x in range(2, n) if n % x == 0)
    # Take first divisor
    d = next(divisors, None)
    if d is None:
        print(n, 'is a prime number')
    else:
        print(n, 'equals', d, '*', n//d)
