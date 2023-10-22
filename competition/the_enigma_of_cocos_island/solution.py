def smallest_prime_factor(n):
    # Check if n is divisible by 2
    if n % 2 == 0:
        return 2

    # Check for prime factors from 3 to the square root of n
    for factor in range(3, int(n**0.5) + 1, 2):
        if n % factor == 0:
            return factor

    # If no prime factor is found, n is a prime number
    return n


def find_AST(n, secret):
    if n == 1:
        return secret
    num = 1
    for i in range(secret, 10**9 + 1):
        if smallest_prime_factor(i) >= secret:
            num += 1
            if num == n:
                return secret * i
    return 0


if __name__ == "__main__":
    number, secret = [int(i) for i in input().split(" ")]
    print(find_AST(number, secret))
