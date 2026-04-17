numbers = [10, 501, 22, 37, 100, 999, 87, 351]

prime_numbers = []

for num in numbers:
    if num > 1:
        is_prime = True
        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            prime_numbers.append(num)

print("Prime numbers:", prime_numbers)
print("Count:", len(prime_numbers))

