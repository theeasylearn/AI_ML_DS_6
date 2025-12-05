print("Prime numbers between 1 and 1000:\n")

# Handle 2 separately (only even prime)
print(2, end=' ')
count = 0  # count total divisibility checks

# Check only odd numbers from 3 to 999
for number in range(3, 1000, 2):
    is_prime = True
    # Only check divisors up to sqrt(number)
    limit = int(number ** 0.5) + 1
    
    # Only check odd divisors starting from 3
    for divisor in range(3, limit, 2):
        count += 1
        if number % divisor == 0:
            is_prime = False
            break
    
    if is_prime:
        print(number, end=' ')

print("\n")
print("Total divisibility checks performed:", count)