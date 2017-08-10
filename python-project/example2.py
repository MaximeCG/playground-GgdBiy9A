# Primality test all the numbers from 2 to 9.
for n in range(2, 10):
    # Look for a divisor of n
    d = None
    for x in range(2, n):
        if n % x == 0:
            d = x
            break
    if d is None:
        # loop fell through without finding a factor
        print(n, 'is a prime number')
    else:
        print(n, 'equals', d, '*', n//d)
