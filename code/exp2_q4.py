def primes_up_to(limit):
    return [num for num in range(2, limit + 1) 
            if all(num % i != 0 for i in range(2, int(num**0.5) + 1))]

print("Prime numbers up to 30:", primes_up_to(30))
