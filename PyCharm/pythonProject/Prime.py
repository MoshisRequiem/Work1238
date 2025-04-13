'''
def facto(n):
    result = 1
    if n <= 0:
        return "Negative Number"
    elif n == 0 or n == 1:
        return result
    else:
        for i in range(2, n+1):
            result *= i
        return result
        #return n * facto(n-1)

print(facto(5))

count = 0
for i in range(2, 101):
    if i % 2  == 0:
        count += 1
print(count)

#Nth fibo
def fib(n):
    if n <= 0:
        return "Enter Valid No."
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    a, b = 0, 1
    for i in range(3, n+1):
        a, b = b, a+b
    return b

print(fib(10))
#facto
def fibo(n):
    a, b = 0, 1
    count = 0
    while count < n:
        yield a
        a, b = b, a+b
        count += 1

print(list(fibo(10)))
def series(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    fi = [0, 1]
    while len(fi) < n:
        fi.append(fi[-1]+fi[-2])
    return fi
print(series(10))

def reverse(n):
    char = list(n)
    left = 0
    right = len(char) - 1
    while left < right:
        char[left], char[right] = char[right], char[left]
        left += 1
        right -= 1
    return ''.join(char)
print(reverse("Python"))

def root(n, e= 1e-7):
    if n < 0:
        return "enter +ve value"
    elif n == 0:
        return 0
    x = n
    while True:
        x1 = (x + n/x)/2
        if abs(x-x1) < e:
            return x1
        x = x1
print(root(2))
'''
import math
def is_prime(n):
    lst = []
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            lst.append(i)
            return False
    return True

print(is_prime(17))
def find_factors(n):
    factors = []
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            factors.append(i)
            if i != n // i:
                factors.append(n // i)
    return sorted(factors)
print(find_factors(20))
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