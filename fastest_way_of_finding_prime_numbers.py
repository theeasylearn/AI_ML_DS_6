def sieve_primes(n):
    if n < 2:
        return []
    
    # Create boolean array and initialize all as True
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    
    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]:
            # Mark multiples of i as not prime
            for j in range(i*i, n+1, i):
                is_prime[j] = False
    
    # Collect and print primes
    primes = [i for i in range(2, n+1) if is_prime[i]]
    print(*primes)
    print(f"\nTotal primes found: {len(primes)}")

print("Prime numbers up to 1000:")
sieve_primes(1000000)