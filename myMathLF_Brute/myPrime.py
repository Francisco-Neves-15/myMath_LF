def list_primes_up_to(limit):
    def is_prime(num):
        """Verifica se um número é primo."""
        if num < 2:
            return False
        for x in range(2, int(num**0.5) + 1):
            if (num % x) == 0:
                return False
        return True

    return [num for num in range(2, limit + 1) if is_prime(num)]

limit = int(input("Enter a number to find all prime numbers up to that number: "))
print(list_primes_up_to(limit))