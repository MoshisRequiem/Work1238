"""
# FACTORIAL
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)


def facto(n):
    result = 1
    for i in range(2, n+1):
        result *= i
    return result


print(factorial(int(input("Enter the number 1- "))))
print(facto(int(input("Enter the number 2- "))))
"""
"""
#COUNT 
count = 0
lst = []
for i in range(0, 11):
    if i % 2 == 0:
        count += 1
        lst.append(i)

print(f"Even numbers count is- {count}\nAnd they are {lst}")
"""
"""
# FIBO SERIES
def series(n):
    if n <= 0:
        print("Enter a +ve number")
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        a, b = 0, 1
        for x in range(3, n+1):
            a, b = b, a+b
        return b


for i in range(1, 11):
    print(series(i), end=" ")


def fibo(n):
    a, b = 0, 1
    count = 1
    while count < n:
        yield a
        a, b = b, a+b   
        count += 1


x = fibo(int(input("Enter a number- ")))
print("Series is- ", list(x))


def okay(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    fibo = [0, 1]
    while len(fibo) < n:
        fibo.append(fibo[-1] + fibo[-2])
    return fibo


print(okay(int(input("Enter a number- "))))

"""
"""
# Nth FIBO
def fibonacci_dp(n):
    if n <= 0:
        return 0
    if n == 1:
        return 0
    if n == 2:
        return 1

    fib = [0] * (n + 1)
    fib[1] = 0
    fib[2] = 1

    for i in range(3, n + 1):
        fib[i] = fib[i - 1] + fib[i - 2]

    return fib[n]


print(fibonacci_dp(10))
"""
"""
# STRING REVERSE
def reverse_string_slicing(s):
    return s[::-1]


def reverse_string_manual(s):
    # Convert string to list for mutability
    chars = list(s)
    left, right = 0, len(chars) - 1

    while left < right:
        # Swap characters
        chars[left], chars[right] = chars[right], chars[left]
        left += 1
        right -= 1

    return ''.join(chars)
    
original = "Python"
print(reverse_string_slicing(original))  # nohtyP
print(reverse_string_manual(original))  # nohtyP
"""
"""
#SQUARE ROOT
def newton_sqrt(n, epsilon=1e-7):
    if n < 0:
        raise ValueError("Cannot compute square root of negative number")
    if n == 0:
        return 0
    x = n
    while True:
        next_x = (x + n / x) / 2
        if abs(x - next_x) < epsilon:
            return next_x
        x = next_x


print(newton_sqrt(16))
print(newton_sqrt(2))
"""
"""
#PRIME NUMBER
import math
def find_factors(n):
    factors = []
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            factors.append(i)
            if i != n // i:
                factors.append(n // i)
    return sorted(factors)


def is_prime(n):
    lst = []
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            lst.append(i)
            return False
    return True


print(find_factors(int(input("Enter a number- "))))
print(is_prime(int(input("Enter a number- "))))
"""
"""
# PRIME FACTORS
import math
def prime_factorization(n):
    factors = []

    while n % 2 == 0:
        factors.append(2)
        n //= 2

    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            factors.append(i)
            n //= i

    if n > 2:
        factors.append(n)
    return factors


print(prime_factorization(int(input("Enter a number- "))))
"""
"""
#GCD
def gcd(a, b):
    a,b = abs(a), abs(b)
    while b:
        a, b = b, a % b
    return a


print(gcd(18, 48))
"""
"""
#LCM
def lcm(a, b):
    a, b = abs(a), abs(b)
    c, d = a, b
    while b:
        a, b = b, a % b
    return abs(c * d) // a


print(lcm(4, 10))
"""
"""
def power_naive(base, exponent):
    result = 1
    for _ in range(exponent):
        result *= base
    return result


print(power_naive(2, 0))
"""