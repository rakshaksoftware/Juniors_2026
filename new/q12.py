def prime_numbers(start, end):
    
    primes = []

    for num in range(start, end + 1):

        if num < 2:
            continue

        is_prime = True

        for i in range(2, num):

            if num % i == 0:
                is_prime = False
                break

        if is_prime:
            primes.append(num)

    return primes


# Taking input from user
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

result = prime_numbers(a, b)

print("Prime numbers between", a, "and", b, "are:")
print(result)