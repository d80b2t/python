"""
p.82 | Chapter 1: A Whirlwind Tour of the Python Language
"""

def gen_primes(N):
    """Generate primes up to N"""
    primes = set()
    for n in range(2, N):
        if all(n % p >0 for p in primes):
            primes.add(n)
            yield n

print(*gen_primes(100))
